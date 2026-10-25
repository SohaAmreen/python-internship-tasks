
def get_reply(user_input):
    user_input = user_input.lower().strip()

    if user_input == "hello" or user_input == "hi":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "what is your name":
        return "I'm a simple Python chatbot made by soha."
    elif user_input == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that."

def main():
    print("=== Basic Chatbot === (type 'bye' to exit)")
    while True:
        user_input = input("You: ")
        reply = get_reply(user_input)
        print("Bot:", reply)
        if user_input.lower().strip() == "bye":
            break

main()
