import os
import google.generativeai as genai

# Load API Key for Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
