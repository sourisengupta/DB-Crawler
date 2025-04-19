from langchain.llms import GoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

def ask_gemini(prompt):
    model = GoogleGenerativeAI(model="gemini-pro", api_key=api_key)
    response = model.invoke(prompt)
    return response