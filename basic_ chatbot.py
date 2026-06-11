# Basic Chatbot

print("Welcome to the Chatbot!")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hi!")
    elif user == "hi":
        print("Bot: Hello! How are you?")
    elif user == "how are you":
        print("Bot: I'm fine, thank you!")
    elif user == "what is your name":
        print("Bot: I am a Python Chatbot.")
    elif user == "who created you":
        print("Bot: I was created using Python.")
    elif user == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break
    else:
        print("Bot: Sorry, I don't understand that.")