"""A minimal command-line chatbot in Python."""

from __future__ import annotations


def get_response(user_message: str) -> str:
    """Return a simple rule-based response for a user message."""
    normalized = user_message.strip().lower()

    if not normalized:
        return "Please type something so I can reply."
    if any(greet in normalized for greet in ("hi", "hello", "hey")):
        return "Hi! How can I help you today?"
    if "name" in normalized:
        return "I'm a basic Python chatbot."
    if "help" in normalized:
        return "You can ask me simple questions, or type 'quit' to exit."

    return "I heard you say: " + user_message.strip()


def main() -> None:
    """Run the chatbot loop."""
    print("Basic Python Chatbot")
    print("Type 'quit' to exit.\n")

    while True:
        user_input = input("You: ")
        if user_input.strip().lower() in {"quit", "exit"}:
            print("Bot: Goodbye!")
            break

        print(f"Bot: {get_response(user_input)}")


if __name__ == "__main__":
    main()
