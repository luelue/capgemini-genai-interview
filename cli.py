#!/usr/bin/env python3
"""
Command Line Interface for GenAI Chatbot
"""
import sys
import os

# Add src directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.chatbot import GenAIChatbot
from src.config import Config

def print_banner():
    """Print application banner."""
    print("=" * 60)
    print("🤖 Capgemini GenAI Interview Chatbot - CLI Mode")
    print("=" * 60)
    print("Type 'quit', 'exit', or 'bye' to exit")
    print("Type 'reset' to clear conversation history")
    print("Type 'help' for available commands")
    print("=" * 60)

def print_help():
    """Print help information."""
    print("\nAvailable commands:")
    print("  help    - Show this help message")
    print("  reset   - Clear conversation history")
    print("  history - Show conversation history")
    print("  quit    - Exit the application")
    print("  exit    - Exit the application")
    print("  bye     - Exit the application")
    print()

def print_history(chatbot):
    """Print conversation history."""
    history = chatbot.get_conversation_history()
    if not history:
        print("\nNo conversation history yet.\n")
        return
    
    print("\n" + "=" * 40)
    print("CONVERSATION HISTORY")
    print("=" * 40)
    for message in history:
        role = message["role"].upper()
        content = message["content"]
        print(f"\n{role}: {content}")
    print("=" * 40 + "\n")

def main():
    """Main CLI application."""
    print_banner()
    
    try:
        # Initialize chatbot
        chatbot = GenAIChatbot()
        print("✅ Chatbot initialized successfully!")
        print(f"📋 Using model: {Config.OPENAI_MODEL}")
        
        # Optional system prompt
        system_prompt = input("\nEnter system prompt (or press Enter for default): ").strip()
        if not system_prompt:
            system_prompt = "You are a helpful AI assistant created for a Capgemini interview demonstration."
        
        print(f"\n🤖 System prompt set: {system_prompt}")
        print("\nYou can start chatting now!\n")
        
        while True:
            try:
                # Get user input
                user_input = input("\nYou: ").strip()
                
                if not user_input:
                    continue
                
                # Handle commands
                if user_input.lower() in ['quit', 'exit', 'bye']:
                    print("\n👋 Goodbye! Thanks for trying the Capgemini GenAI Chatbot!")
                    break
                elif user_input.lower() == 'reset':
                    chatbot.reset_conversation()
                    print("\n🔄 Conversation history cleared!")
                    continue
                elif user_input.lower() == 'help':
                    print_help()
                    continue
                elif user_input.lower() == 'history':
                    print_history(chatbot)
                    continue
                
                # Get chatbot response
                print("\n🤖 Assistant: ", end="", flush=True)
                response = chatbot.chat(user_input, system_prompt)
                print(response)
                
            except KeyboardInterrupt:
                print("\n\n👋 Goodbye! Thanks for trying the Capgemini GenAI Chatbot!")
                break
            except Exception as e:
                print(f"\n❌ Error: {str(e)}")
                
    except ValueError as e:
        print(f"\n❌ Configuration Error: {str(e)}")
        print("💡 Please create a .env file with your OpenAI API key. See .env.example for reference.")
        return 1
    except Exception as e:
        print(f"\n❌ Initialization Error: {str(e)}")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())