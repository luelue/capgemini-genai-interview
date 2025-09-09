# Capgemini GenAI Interview Project 🤖

A comprehensive GenAI chatbot demonstration built for the Capgemini interview process. This project showcases modern AI integration, web development, and software engineering best practices.

## 🚀 Features

- **AI-Powered Chatbot**: Integration with OpenAI's GPT models for intelligent conversations
- **Dual Interface**: Both web (Streamlit) and command-line interfaces
- **Conversation Memory**: Maintains context across multiple exchanges
- **Configurable System Prompts**: Customize chatbot behavior for different use cases
- **Professional UI**: Clean, responsive web interface with Capgemini branding
- **Error Handling**: Robust error handling and user feedback
- **Logging**: Comprehensive logging for debugging and monitoring
- **Testing**: Unit tests for core functionality

## 🛠️ Technology Stack

- **Backend**: Python 3.8+
- **AI/ML**: OpenAI GPT API
- **Web Framework**: Streamlit
- **Environment Management**: python-dotenv
- **Testing**: pytest
- **Version Control**: Git

## 📋 Prerequisites

- Python 3.8 or higher
- OpenAI API key
- pip (Python package manager)

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/luelue/capgemini-genai-interview.git
   cd capgemini-genai-interview
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   ```
   Edit `.env` and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_actual_api_key_here
   OPENAI_MODEL=gpt-3.5-turbo
   MAX_TOKENS=150
   TEMPERATURE=0.7
   ```

## 🚀 Usage

### Web Interface (Streamlit)

Launch the web application:
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

**Features:**
- Interactive chat interface
- Configurable system prompts
- Conversation history
- Reset functionality
- Real-time responses

### Command Line Interface

Run the CLI version:
```bash
python cli.py
```

**Available Commands:**
- `help` - Show available commands
- `reset` - Clear conversation history
- `history` - Show conversation history
- `quit/exit/bye` - Exit the application

## 🧪 Testing

Run the test suite:
```bash
pytest tests/ -v
```

Run tests with coverage:
```bash
pytest tests/ --cov=src --cov-report=html
```

## 📁 Project Structure

```
capgemini-genai-interview/
├── src/
│   ├── config.py          # Configuration management
│   └── chatbot.py         # Core chatbot functionality
├── tests/
│   ├── test_config.py     # Configuration tests
│   └── test_chatbot.py    # Chatbot functionality tests
├── docs/
│   └── example_prompts.md # Example prompts and use cases
├── app.py                 # Streamlit web interface
├── cli.py                 # Command line interface
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
├── .gitignore            # Git ignore rules
└── README.md             # This file
```

## 💡 Example Use Cases

The chatbot is designed to demonstrate various consulting scenarios:

1. **Business Analysis**: Market research, competitive analysis
2. **Technical Consulting**: Cloud migration, data strategy
3. **Industry Expertise**: Financial services, healthcare, manufacturing
4. **Innovation**: AI ethics, sustainability consulting
5. **Problem Solving**: Crisis management, change management

See [example_prompts.md](docs/example_prompts.md) for detailed examples.

## 🔧 Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `OPENAI_API_KEY` | Your OpenAI API key | Required |
| `OPENAI_MODEL` | GPT model to use | `gpt-3.5-turbo` |
| `MAX_TOKENS` | Maximum response tokens | `150` |
| `TEMPERATURE` | Response creativity (0-2) | `0.7` |

### Customization

1. **System Prompts**: Modify the default system prompt in the web interface or CLI
2. **Model Parameters**: Adjust temperature and max tokens in `.env`
3. **UI Styling**: Customize CSS in `app.py` for different branding
4. **Conversation History**: Modify history length in `chatbot.py`

## 🚀 Deployment

### Local Development
```bash
streamlit run app.py
```

### Production Deployment

1. **Streamlit Cloud**: Deploy directly from GitHub
2. **Docker**: Create a Dockerfile for containerized deployment
3. **Heroku**: Use Heroku for cloud deployment
4. **AWS/Azure/GCP**: Deploy on major cloud platforms

### Docker Deployment (Optional)

Create a `Dockerfile`:
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

Build and run:
```bash
docker build -t capgemini-genai-chatbot .
docker run -p 8501:8501 --env-file .env capgemini-genai-chatbot
```

## 🔍 Troubleshooting

### Common Issues

1. **API Key Error**
   - Ensure your OpenAI API key is correctly set in `.env`
   - Verify the API key has sufficient credits

2. **Module Import Error**
   - Ensure you're in the project root directory
   - Verify all dependencies are installed

3. **Streamlit Port Conflict**
   - Use a different port: `streamlit run app.py --server.port=8502`

4. **Environment Variables Not Loading**
   - Ensure `.env` file is in the project root
   - Check file permissions and formatting

## 📈 Future Enhancements

- [ ] Multi-model support (Claude, Gemini)
- [ ] Document upload and analysis
- [ ] Voice input/output
- [ ] Advanced conversation analytics
- [ ] Role-based access control
- [ ] Integration with enterprise systems
- [ ] Conversation export functionality
- [ ] Multi-language support

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is created for the Capgemini interview process and is intended for demonstration purposes.

## 👨‍💻 Author

Created for the Capgemini GenAI Interview Process

---

**Note**: This is a demonstration project showcasing GenAI integration, web development, and software engineering best practices for interview purposes.