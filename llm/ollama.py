from typing import List
from llm.base import LLM
from core.models import Message, LLMResponse
from ollama import chat

class OllamaLLM(LLM):

    def __init__(self, model: str = "llama3.1:8b"):
        self.model = model
    
    def chat(self, messages: List[Message]) -> LLMResponse:
        message_dicts = [{"role": msg.role, "content": msg.content} for msg in messages]
        response = chat(model=self.model, messages=message_dicts)

        return LLMResponse(
            content=response.message.content,
            model=self.model
        )

