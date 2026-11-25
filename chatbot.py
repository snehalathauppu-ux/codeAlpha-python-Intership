
def chatbot():
    print("Welcome to Python Chatbot!")
    print("You can type: hello, how are you, bye")

    while True:
        user = input("You: ").lower()

        if user == "hello":
            print("Bot: Hi! Welcome!")

        elif user == "how are you":
            print("Bot: I am fine. How are you?")

        elif user == "what is your name":
            print("Bot: I am Python Chatbot.")

        elif user == "thank you":
            print("Bot: You are welcome!")

        elif user == "bye":
            print("Bot: Goodbye! Have a nice day!")
            break

        else:
            print("Bot: Sorry, I don't understand.")

chatbot()
