import random


class SimpleChatbot:
    def __init__(self):
        self.responses = {
            "greeting": ["Hello!", "Hi there!", "How can I help you today?"],
            "help": ["Sure! What do you need assistance with?", "How can I assist you?", "What can I do for you today?"],
            "goodbye": ["Goodbye!", "See you later!", "Have a great day!"],
            "default": ["Sorry, I didn't understand that.", "Can you please rephrase?", "I'm not sure about that."]
        }
        
    def get_response(self, user_input):
        user_input = user_input.lower()
        
        if "hello" in user_input or "hi" in user_input:
            return random.choice(self.responses["greeting"])
        elif "help" in user_input:
            return random.choice(self.responses["help"])
        elif "bye" in user_input or "goodbye" in user_input:
            return random.choice(self.responses["goodbye"])
        else:
            return random.choice(self.responses["default"])


def chatbot_interaction():
    chatbot = SimpleChatbot()
    print("Chatbot: Hello! How can I assist you today?")
    
    while True:
        user_input = input("You: ")
        if "bye" in user_input.lower() or "goodbye" in user_input.lower():
            print("Chatbot: Goodbye!")
            break
        else:
            response = chatbot.get_response(user_input)
            print(f"Chatbot: {response}")


if __name__ == "__main__":
    chatbot_interaction()
