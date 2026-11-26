from langchain_google_genai import ChatGoogleGenerativeAI
from app.core.config import settings

def get_llm():

    return ChatGoogleGenerativeAI(
        model=settings.GEMINI_MODEL,
        google_api_key=settings.GOOGLE_API_KEY,
        temperature=0.2,
        max_retries=3
    )