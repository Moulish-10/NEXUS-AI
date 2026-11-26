from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.llm.provider import get_llm

router = APIRouter()


class ChatRequest(BaseModel):
    message: str


@router.post("/chat")
async def chat(request: ChatRequest):

    try:
        llm = get_llm()

        response = await llm.ainvoke(
            request.message
        )

        return {
            "success": True,
            "model": "gemini",
            "response": response.content
        }

    except Exception:
        raise HTTPException(
            status_code=502,
            detail="Gemini request failed. Check API configuration and service availability."
        )