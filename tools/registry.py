import json
from typing import Dict
from tools.base import Tool


class ToolRegistry:
    def __init__(self):
        self._tools: Dict[str, Tool] = {}

    def register(self, tool: Tool):
        self._tools[tool.name] = tool

    def get(self, name: str) -> Tool | None:
        return self._tools.get(name)

    def schema(self) -> str:
        tools = [
            {
                "name": tool.name,
                "description": tool.description,
                "parameters": tool.schema(),
            }
            for tool in self._tools.values()
        ]
        return json.dumps(tools)
