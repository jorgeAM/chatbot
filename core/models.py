from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class Message:
    role: str
    content: str | None


@dataclass
class ToolCall:
    name: str
    arguments: Dict[str, Any]


@dataclass
class LLMResponse:
    content: str | None = None
    tool_call: ToolCall | None = None
    tokens_used: int | None = None
    model: str | None = None
