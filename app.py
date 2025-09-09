"""
Streamlit Web Interface for GenAI Chatbot
"""
import streamlit as st
import sys
import os

# Add src directory to path so we can import our modules
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.chatbot import GenAIChatbot
from src.config import Config

# Page configuration
st.set_page_config(
    page_title="Capgemini GenAI Chatbot",
    page_icon="🤖",
    layout="wide"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f4e79;
        text-align: center;
        margin-bottom: 2rem;
    }
    .chat-message {
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
    .user-message {
        background-color: #e8f4f8;
        border-left: 4px solid #1f4e79;
    }
    .assistant-message {
        background-color: #f0f8f0;
        border-left: 4px solid #4caf50;
    }
</style>
""", unsafe_allow_html=True)

def initialize_chatbot():
    """Initialize the chatbot and handle errors."""
    try:
        if 'chatbot' not in st.session_state:
            st.session_state.chatbot = GenAIChatbot()
        return True
    except ValueError as e:
        st.error(f"Configuration Error: {str(e)}")
        st.info("Please create a .env file with your OpenAI API key. See .env.example for reference.")
        return False
    except Exception as e:
        st.error(f"Initialization Error: {str(e)}")
        return False

def main():
    """Main Streamlit application."""
    
    # Header
    st.markdown('<h1 class="main-header">🤖 Capgemini GenAI Interview Chatbot</h1>', unsafe_allow_html=True)
    
    # Description
    st.markdown("""
    This is a demonstration GenAI chatbot built for the Capgemini interview process. 
    It uses OpenAI's GPT models to provide intelligent responses to your questions.
    """)
    
    # Initialize chatbot
    if not initialize_chatbot():
        return
    
    # Sidebar for configuration
    with st.sidebar:
        st.header("Configuration")
        
        # System prompt
        system_prompt = st.text_area(
            "System Prompt (Optional)",
            value="You are a helpful AI assistant created for a Capgemini interview demonstration.",
            help="This sets the behavior and personality of the chatbot"
        )
        
        # Model info
        st.info(f"**Model:** {Config.OPENAI_MODEL}")
        st.info(f"**Max Tokens:** {Config.MAX_TOKENS}")
        st.info(f"**Temperature:** {Config.TEMPERATURE}")
        
        # Reset conversation button
        if st.button("🔄 Reset Conversation"):
            st.session_state.chatbot.reset_conversation()
            if 'messages' in st.session_state:
                del st.session_state.messages
            st.success("Conversation reset!")
            st.rerun()
    
    # Initialize chat history
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    
    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Type your message here..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Get bot response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = st.session_state.chatbot.chat(prompt, system_prompt if system_prompt else None)
            st.markdown(response)
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666; font-size: 0.9rem;'>
        Built with ❤️ for Capgemini GenAI Interview | Powered by OpenAI GPT
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()