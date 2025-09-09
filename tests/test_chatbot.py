"""
Tests for the GenAI Chatbot Core Module
"""
import pytest
import sys
import os
from unittest.mock import Mock, patch

# Add src to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from src.chatbot import GenAIChatbot

class TestGenAIChatbot:
    """Test cases for the GenAIChatbot class."""
    
    @patch('src.chatbot.openai.OpenAI')
    @patch('src.chatbot.Config')
    def test_init_success(self, mock_config, mock_openai):
        """Test successful initialization of chatbot."""
        mock_config.validate.return_value = True
        mock_config.OPENAI_API_KEY = 'test-key'
        mock_config.OPENAI_MODEL = 'gpt-3.5-turbo'
        mock_config.MAX_TOKENS = 150
        mock_config.TEMPERATURE = 0.7
        
        chatbot = GenAIChatbot()
        
        assert chatbot.model == 'gpt-3.5-turbo'
        assert chatbot.max_tokens == 150
        assert chatbot.temperature == 0.7
        assert chatbot.conversation_history == []
    
    @patch('src.chatbot.Config')
    def test_init_config_validation_fails(self, mock_config):
        """Test initialization fails when config validation fails."""
        mock_config.validate.side_effect = ValueError("API key missing")
        
        with pytest.raises(ValueError):
            GenAIChatbot()
    
    @patch('src.chatbot.openai.OpenAI')
    @patch('src.chatbot.Config')
    def test_reset_conversation(self, mock_config, mock_openai):
        """Test conversation reset functionality."""
        mock_config.validate.return_value = True
        mock_config.OPENAI_API_KEY = 'test-key'
        mock_config.OPENAI_MODEL = 'gpt-3.5-turbo'
        mock_config.MAX_TOKENS = 150
        mock_config.TEMPERATURE = 0.7
        
        chatbot = GenAIChatbot()
        chatbot.conversation_history = [{"role": "user", "content": "test"}]
        
        chatbot.reset_conversation()
        
        assert chatbot.conversation_history == []
    
    @patch('src.chatbot.openai.OpenAI')
    @patch('src.chatbot.Config')
    def test_get_conversation_history(self, mock_config, mock_openai):
        """Test getting conversation history."""
        mock_config.validate.return_value = True
        mock_config.OPENAI_API_KEY = 'test-key'
        mock_config.OPENAI_MODEL = 'gpt-3.5-turbo'
        mock_config.MAX_TOKENS = 150
        mock_config.TEMPERATURE = 0.7
        
        chatbot = GenAIChatbot()
        test_history = [{"role": "user", "content": "test"}]
        chatbot.conversation_history = test_history
        
        history = chatbot.get_conversation_history()
        
        assert history == test_history
        # Ensure it returns a copy, not the original
        assert history is not chatbot.conversation_history
    
    @patch('src.chatbot.openai.OpenAI')
    @patch('src.chatbot.Config')
    def test_chat_basic_functionality(self, mock_config, mock_openai):
        """Test basic chat functionality with mocked OpenAI response."""
        mock_config.validate.return_value = True
        mock_config.OPENAI_API_KEY = 'test-key'
        mock_config.OPENAI_MODEL = 'gpt-3.5-turbo'
        mock_config.MAX_TOKENS = 150
        mock_config.TEMPERATURE = 0.7
        
        # Mock OpenAI response
        mock_response = Mock()
        mock_response.choices = [Mock()]
        mock_response.choices[0].message.content = "Hello! How can I help you?"
        
        mock_client = Mock()
        mock_client.chat.completions.create.return_value = mock_response
        mock_openai.return_value = mock_client
        
        chatbot = GenAIChatbot()
        response = chatbot.chat("Hello")
        
        assert response == "Hello! How can I help you?"
        assert len(chatbot.conversation_history) == 2  # user + assistant
        assert chatbot.conversation_history[0]["role"] == "user"
        assert chatbot.conversation_history[1]["role"] == "assistant"
    
    @patch('src.chatbot.openai.OpenAI')
    @patch('src.chatbot.Config')
    def test_chat_with_system_prompt(self, mock_config, mock_openai):
        """Test chat functionality with system prompt."""
        mock_config.validate.return_value = True
        mock_config.OPENAI_API_KEY = 'test-key'
        mock_config.OPENAI_MODEL = 'gpt-3.5-turbo'
        mock_config.MAX_TOKENS = 150
        mock_config.TEMPERATURE = 0.7
        
        # Mock OpenAI response
        mock_response = Mock()
        mock_response.choices = [Mock()]
        mock_response.choices[0].message.content = "I'm a helpful assistant."
        
        mock_client = Mock()
        mock_client.chat.completions.create.return_value = mock_response
        mock_openai.return_value = mock_client
        
        chatbot = GenAIChatbot()
        response = chatbot.chat("Hello", "You are a helpful assistant.")
        
        # Verify the API was called with system message
        call_args = mock_client.chat.completions.create.call_args[1]
        messages = call_args['messages']
        assert messages[0]["role"] == "system"
        assert messages[0]["content"] == "You are a helpful assistant."
        assert messages[1]["role"] == "user"
        assert messages[1]["content"] == "Hello"