from abc import ABC, abstractmethod
from typing import List
from core.models import Message,LLMResponse

class LLM(ABC):
    @abstractmethod
    def chat(self, messages: List[Message]) -> LLMResponse:
        pass
