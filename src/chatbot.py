"""
GenAI Chatbot Core Module
"""
import openai
import logging
from typing import List, Dict, Optional
from .config import Config

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class GenAIChatbot:
    """A simple GenAI chatbot using OpenAI's API."""
    
    def __init__(self):
        """Initialize the chatbot with configuration."""
        Config.validate()
        self.client = openai.OpenAI(api_key=Config.OPENAI_API_KEY)
        self.model = Config.OPENAI_MODEL
        self.max_tokens = Config.MAX_TOKENS
        self.temperature = Config.TEMPERATURE
        self.conversation_history: List[Dict[str, str]] = []
        
    def chat(self, user_message: str, system_prompt: Optional[str] = None) -> str:
        """
        Send a message to the chatbot and get a response.
        
        Args:
            user_message: The user's message
            system_prompt: Optional system prompt to set behavior
            
        Returns:
            The chatbot's response
        """
        try:
            # Build messages for the API call
            messages = []
            
            # Add system prompt if provided
            if system_prompt:
                messages.append({"role": "system", "content": system_prompt})
            
            # Add conversation history
            messages.extend(self.conversation_history)
            
            # Add current user message
            messages.append({"role": "user", "content": user_message})
            
            # Make API call
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                max_tokens=self.max_tokens,
                temperature=self.temperature
            )
            
            # Extract response text
            assistant_message = response.choices[0].message.content
            
            # Update conversation history
            self.conversation_history.append({"role": "user", "content": user_message})
            self.conversation_history.append({"role": "assistant", "content": assistant_message})
            
            # Keep conversation history manageable (last 10 exchanges)
            if len(self.conversation_history) > 20:
                self.conversation_history = self.conversation_history[-20:]
            
            logger.info(f"User: {user_message}")
            logger.info(f"Assistant: {assistant_message}")
            
            return assistant_message
            
        except Exception as e:
            logger.error(f"Error in chat: {str(e)}")
            return f"Sorry, I encountered an error: {str(e)}"
    
    def reset_conversation(self):
        """Reset the conversation history."""
        self.conversation_history = []
        logger.info("Conversation history reset")
    
    def get_conversation_history(self) -> List[Dict[str, str]]:
        """Get the current conversation history."""
        return self.conversation_history.copy()