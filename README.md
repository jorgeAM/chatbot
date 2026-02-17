# AI Agent Chatbot

A simple AI agent chatbot built with Python that uses Ollama for LLM inference and supports tool calling for extended functionality.

## Features

- Conversational AI agent with memory
- Tool calling support for extended capabilities
- Modular architecture with pluggable LLM backends
- Easy tool registration system

## Prerequisites

- Python 3.14+
- [Ollama](https://ollama.ai) installed and running
- uv package manager

## Installation

1. Clone the repository
2. Install dependencies:

```bash
uv sync
```

3. Pull the default Ollama model:

```bash
ollama pull llama3.1:8b
```

## Usage

Run the chatbot:

```bash
uv run main.py
```

Type your messages and press Enter. Type `exit` to quit.

## Architecture

### Core Components

- `core/agent.py` - Main agent orchestration with conversation memory
- `core/models.py` - Data models (Message, ToolCall, LLMResponse)

### LLM Layer

- `llm/base.py` - Abstract LLM interface
- `llm/ollama.py` - Ollama implementation with tool calling support

### Tools System

- `tools/base.py` - Abstract Tool interface
- `tools/registry.py` - Tool registration and schema generation
- `tools/sales_tool.py` - Example tool that returns sales data

## Adding New Tools

Create a new tool by extending the `Tool` base class:

```python
from tools.base import Tool

class MyTool(Tool):
    name = "my_tool"
    description = "Description of what this tool does"

    def execute(self, arguments):
        # Your tool logic here
        return "result"
```

Register it in `main.py`:

```python
tools.register(MyTool())
```

## Model Configuration

The default model is `llama3.1:8b`. To use a different model:

```python
llm = OllamaLLM(model="qwen2.5:14b")
```

Recommended models for better tool calling:

- `qwen2.5:14b` or `qwen2.5:32b` - Excellent tool calling performance
- `llama3.1:70b` - Better than 8b but requires more resources
- `mistral:7b` - Good alternative at similar size

## How It Works

1. User sends a message
2. Agent adds message to conversation memory
3. LLM receives conversation history + available tools schema
4. If LLM decides to use a tool:
   - Returns JSON with tool name and arguments
   - Agent executes the tool
   - Tool result is added to memory
   - LLM generates final response based on tool result
5. If no tool needed, LLM responds directly
6. Response is shown to user and added to memory

## Project Structure

```
.
├── core/
│   ├── agent.py       # Agent orchestration
│   └── models.py      # Data models
├── llm/
│   ├── base.py        # LLM interface
│   └── ollama.py      # Ollama implementation
├── tools/
│   ├── base.py        # Tool interface
│   ├── registry.py    # Tool management
│   └── sales_tool.py  # Example tool
├── main.py            # Entry point
└── pyproject.toml     # Dependencies
```

## License

MIT
