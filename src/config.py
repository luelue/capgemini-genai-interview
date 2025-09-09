"""
GenAI Chatbot Configuration Module
"""
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Configuration class for the GenAI chatbot application."""
    
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    OPENAI_MODEL = os.getenv('OPENAI_MODEL', 'gpt-3.5-turbo')
    MAX_TOKENS = int(os.getenv('MAX_TOKENS', 150))
    TEMPERATURE = float(os.getenv('TEMPERATURE', 0.7))
    
    @classmethod
    def validate(cls):
        """Validate that required configuration is present."""
        if not cls.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY is required. Please set it in your .env file.")
        return True