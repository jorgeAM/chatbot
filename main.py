from llm.ollama import OllamaLLM
from core.models import Message
from core.agent import Agent
from tools.registry import ToolRegistry
from tools.sales_tool import GetSalesToday

def main():
    llm = OllamaLLM()
    tools = ToolRegistry()
    tools.register(GetSalesToday())
    agent = Agent(llm=llm, tools=tools)
    print("AI Agent Started. Type 'exit' to quit\n")


    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        response = agent.handle_user_message(user_input)
        print(f"Agent: {response} \n")


if __name__ == "__main__":
    main()
