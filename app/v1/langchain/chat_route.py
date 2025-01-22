import json

from fastapi import APIRouter, HTTPException, status
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_groq import ChatGroq

from app.core.config import settings

router = APIRouter(prefix="/chat", tags=["chat"])

model = ChatGroq(model="llama-3.3-70b-versatile", api_key=settings.GROQ_API_KEY)


@router.post("/chat")
def chat():
    try:
        messages = [
            SystemMessage("Translate the following from English into French"),
            HumanMessage("hi!"),
        ]

        response = model.invoke(messages)

        formatted_response = json.dumps(response.model_dump(), indent=4)
        return formatted_response
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )
