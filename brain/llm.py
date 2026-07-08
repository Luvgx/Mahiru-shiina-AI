import os
from dotenv import load_dotenv
import google.generativeai as genai
from config import MODEL_NAME
from brain.prompts import SYSTEM_PROMPT


def load_api_key():
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in .env file.")
    return api_key

def initialize_model():
    api_key = load_api_key()
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(MODEL_NAME)
    return model

def generate_response(model, user_prompt):
    if not user_prompt.strip():
        return "Please say something."
    final_prompt = f"""{SYSTEM_PROMPT} user: {user_prompt}"""
    try:
        response = model.generate_content(final_prompt)
        return response.text
    except Exception as e:
        print(f"Error generating response: {e}")
        return None

def chat(user_prompt):
    try:
        model = initialize_model()
        response = generate_response(model, user_prompt)
        return response
    except Exception as e:
        print(f"Error in chat(): {e}")
        return None