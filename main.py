from voice.speak import speak
from brain.llm import chat
from voice.listen import listen
def main():
    print("=" * 50)
    print("🤖 Shiina AI Assistant")
    print("Type 'exit' to quit.")
    print("=" * 50)

    while True:
            user_prompt = listen()

            if not user_prompt:
                 continue
            if user_prompt and user_prompt.lower() in ["exit", "EXIT", "quit", "QUIT", "Bye", "Sayoonara"]:
                print("Shiina: Goodbye Siddhant! 👋")
                break

            response = chat(user_prompt)

            if response:
                print(f"\nShiina: {response}")
                speak(response)
            else:
                print("\nShiina: Sorry, I couldn't generate a response.")
if __name__ == "__main__":
    main()
