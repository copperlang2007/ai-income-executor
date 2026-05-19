# config.py - Add your API keys here (use .env in production)
import os
from dotenv import load_dotenv  # pip install python-dotenv (user side)

load_dotenv()

# AI Providers
XAI_API_KEY = os.getenv("XAI_API_KEY", "your-grok-key-here")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your-openai-key")
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY", "your-elevenlabs-key")
IDEOGRAM_API_KEY = os.getenv("IDEOGRAM_API_KEY", "")  # or Midjourney via Discord

# Platform APIs (add as needed)
ETSY_API_KEY = os.getenv("ETSY_API_KEY", "")
GUMROAD_API_KEY = os.getenv("GUMROAD_API_KEY", "")

# Paths
DATA_DIR = "data"
SCRIPTS_DIR = "scripts"

print("Config loaded. Replace placeholders with real keys for full functionality.")