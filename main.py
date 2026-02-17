from llm.ollama import OllamaLLM
from core.models import Message

def main():
    llm = OllamaLLM()
    response = llm.chat(messages=[Message(role="user", content="tell me a joke")])
    print(response)


if __name__ == "__main__":
    main()
