from llm.base import LLM
from core.models import Message
from typing import List, Optional
from tools.registry import ToolRegistry


class Agent:
    def __init__(self, llm: LLM, tools: ToolRegistry):
        self.llm = llm
        self.tools = tools
        self.memory: List[Message] = []

    def handle_user_message(self, user_input: str) -> Optional[str]:
        self.memory.append(Message(role="user", content=user_input))

        response = self.llm.chat(self.memory, tools_schema=self.tools.schema())

        if response.tool_call:
            tool = self.tools.get(response.tool_call.name)
            if not tool:
                return "Tool not found"

            result = tool.execute(response.tool_call.arguments)
            self.memory.append(
                Message(role="assistant", content=f"Tool result: {result}")
            )

            final_response = self.llm.chat(self.memory)
            self.memory.append(
                Message(role="assistant", content=final_response.content)
            )

            return final_response.content

        self.memory.append(Message(role="assistant", content=response.content))

        return response.content
