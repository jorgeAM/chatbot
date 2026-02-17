from ollama import chat


def main():
    print("Hello from chatbot!")

    response = chat(
        model="llama3.1:8b", messages=[{"role": "user", "content": "tell me a joke"}]
    )

    print(response)


if __name__ == "__main__":
    main()
