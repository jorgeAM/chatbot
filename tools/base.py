from pydantic import BaseModel
from abc import ABC, abstractmethod
from typing import Any, Type


class Tool(ABC):
    name: str
    description: str
    args_model: Type[BaseModel]

    def validate(self, arguments: dict):
        return self.args_model(**arguments)

    @abstractmethod
    def execute(self, arguments: BaseModel) -> Any:
        pass

    def schema(self) -> dict:
        return self.args_model.model_json_schema()
