"""
Tests for the GenAI Chatbot Configuration
"""
import pytest
import os
import sys

# Add src to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from src.config import Config

class TestConfig:
    """Test cases for the Config class."""
    
    def test_config_attributes_exist(self):
        """Test that all required config attributes exist."""
        assert hasattr(Config, 'OPENAI_API_KEY')
        assert hasattr(Config, 'OPENAI_MODEL')
        assert hasattr(Config, 'MAX_TOKENS')
        assert hasattr(Config, 'TEMPERATURE')
    
    def test_default_values(self):
        """Test that default values are set correctly."""
        # These should have defaults even without env vars
        assert Config.OPENAI_MODEL == 'gpt-3.5-turbo'
        assert Config.MAX_TOKENS == 150
        assert Config.TEMPERATURE == 0.7
    
    def test_validate_method_exists(self):
        """Test that validate method exists."""
        assert hasattr(Config, 'validate')
        assert callable(Config.validate)
    
    def test_validate_with_missing_api_key(self, monkeypatch):
        """Test validation fails when API key is missing."""
        # Remove API key from environment
        monkeypatch.delenv('OPENAI_API_KEY', raising=False)
        monkeypatch.setattr(Config, 'OPENAI_API_KEY', None)
        
        with pytest.raises(ValueError) as excinfo:
            Config.validate()
        
        assert "OPENAI_API_KEY is required" in str(excinfo.value)
    
    def test_validate_with_api_key(self, monkeypatch):
        """Test validation passes when API key is present."""
        # Set a dummy API key
        monkeypatch.setattr(Config, 'OPENAI_API_KEY', 'test-api-key')
        
        # Should not raise an exception
        result = Config.validate()
        assert result is True