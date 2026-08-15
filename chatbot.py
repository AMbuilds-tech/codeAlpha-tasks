"""
Task 4: Basic Rule-Based Chatbot
A simple chatbot that responds to predefined user inputs using if-elif logic.
"""


def get_response(user_input):
    """
    Takes user input, normalizes it, and returns a predefined reply
    based on matching keywords/phrases.
    """
    # Normalize input: lowercase and strip extra spaces
    text = user_input.lower().strip()

    if text in ("hello", "hi", "hey"):
        return "Hi!"

    elif text in ("how are you", "how are you?"):
        return "I'm fine, thanks!"

    elif text in ("what is your name", "what's your name", "who are you"):
        return "I'm a simple rule-based chatbot!"

    elif text in ("help", "what can you do"):
        return "You can say: hello, how are you, your name, or bye."

    elif text in ("bye", "goodbye", "exit", "quit"):
        return "Goodbye!"

    else:
        return "Sorry, I didn't understand that. Type 'help' to see what I can do."


def chat():
    """
    Runs the main chatbot loop: takes input, prints a reply,
    and stops when the user says bye/exit/quit.
    """
    print("Chatbot: Hi! Type 'bye' anytime to end the chat.")

    while True:
        user_input = input("You: ")

        reply = get_response(user_input)
        print("Chatbot:", reply)

        # End the loop if user wants to exit
        if user_input.lower().strip() in ("bye", "goodbye", "exit", "quit"):
            break


if __name__ == "__main__":
    chat()
