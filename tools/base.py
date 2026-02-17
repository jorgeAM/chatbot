from abc import ABC, abstractmethod
from typing import Dict, Any


class Tool(ABC):
    name: str
    description: str

    @abstractmethod
    def execute(self, arguments: Dict[str, Any]) -> Any:
        pass

