import os
from dotenv import load_dotenv

load_dotenv()


PORT = os.getenv("PORT", "8900")  # Default port


GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
