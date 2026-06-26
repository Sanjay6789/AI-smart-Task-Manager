import os
from dotenv import load_dotenv

# .env file se keys load karne ke liye
load_dotenv()

# Groq API Key configuration
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "YOUR_GROQ_API_KEY_HERE")

# Model configuration
MODEL_NAME = "llama-3.1-8b-instant"