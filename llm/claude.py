import json
import anthropic
from anthropic.types import MessageParam
from typing import cast
from llm.base import LLM
from core.models import Message, LLMResponse, ToolCall


class ClaudeLLM(LLM):
    def __init__(self):
        self.client = anthropic.Anthropic()
        self.model = "claude-sonnet-4-5"

    def chat(
        self, messages: list[Message], tools_schema: str | None = None
    ) -> LLMResponse:
        kwargs: dict = {}
        if tools_schema:
            tools_data = json.loads(tools_schema)
            kwargs["tools"] = [
                {
                    "name": t["name"],
                    "description": t["description"],
                    "input_schema": t["parameters"],
                }
                for t in tools_data
            ]

        message = self.client.messages.create(
            model=self.model,
            max_tokens=1000,
            messages=[
                cast(MessageParam, {"role": msg.role, "content": msg.content or ""})
                for msg in messages
            ],
            **kwargs,
        )

        tokens_used = message.usage.input_tokens + message.usage.output_tokens

        for block in message.content:
            if block.type == "tool_use":
                return LLMResponse(
                    tool_call=ToolCall(name=block.name, arguments=block.input),
                    model=self.model,
                    tokens_used=tokens_used,
                )

        content = ""
        for block in message.content:
            if block.type == "text":
                content = block.text
                break

        return LLMResponse(
            content=content,
            model=self.model,
            tokens_used=tokens_used,
        )
