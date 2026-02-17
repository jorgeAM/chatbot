import json
from typing import List
from llm.base import LLM
from core.models import Message, LLMResponse, ToolCall
from ollama import chat


class OllamaLLM(LLM):
    def __init__(self, model: str = "llama3.1:8b"):
        self.model = model

    def chat(
        self, messages: List[Message], tools_schema: str | None = None
    ) -> LLMResponse:
        system_prompt = """You're an AI assistant with access to tools.

        When you need to use a tool, respond ONLY with valid JSON in this exact format:
        {
            "tool": "tool_name",
            "arguments": {}
        }

        When no tool is needed, respond normally in plain text.

        IMPORTANT: Use the available tools when the user asks for information that requires them."""

        if tools_schema:
            system_prompt += f"\n\nAvailable tools:\n{tools_schema}"

        message_dicts = [{"role": "system", "content": system_prompt}]
        message_dicts.extend(
            [{"role": msg.role, "content": msg.content or ""} for msg in messages]
        )

        response = chat(model=self.model, messages=message_dicts)

        response_content = response.message.content or ""

        try:
            content = json.loads(response_content)
            if "tool" in content:
                return LLMResponse(
                    tool_call=ToolCall(
                        name=content["tool"], arguments=content.get("arguments", {})
                    )
                )
        except Exception:
            pass

        return LLMResponse(content=response_content, model=self.model)
