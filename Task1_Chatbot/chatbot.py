from datetime import datetime
def get_response(message):
  message = message.lower().strip()
  
  if "hello" in message or "hi" in message or "hey" in message:
        return "Hello! Nice to meet you. How can I help you?"
  elif "how are you" in message:
        return "I'm doing good! Thanks for asking."
  elif "your name" in message or "who are you" in message:
        return "I'm a simple rule-based chatbot created using Python."
  elif "president of india" in message:
        return"Droupadi Murmu is the 15th and current President of India."
  elif "chief minister of tamilnadu" in message or "cm of tamilnadu" in message:
        return"The Chief Minister of Tamil Nadu is C. Joseph Vijay. He is the founder of the Tamilaga Vettri Kazhagam (TVK)."
  elif "time" in message:
        currenttime = datetime.now().strftime("%I:%M %p")
        return "The current time is " + currenttime
  elif "date" in message or "today" in message:
        currentdate = datetime.now().strftime("%d %B %Y")
        return "Today's date is " + currentdate
  elif "help" in message or "what can you do" in message:
        return "I can respond to you, tell you the date and time, and have a simple conversation."
  elif "thank" in message:
        return "You're welcome!"
  elif "sad" in message or "bad" in message or "sorry" in message:
        return "I'm sorry to hear that. I hope things get better soon."
  else:
       return "I'm still learning. I don't have a response for that."

print("\nWelcome to ChitChat")
print("You can ask me a few basic questions.")
print("Type 'bye' to exit.\n")


while True:
    usermessage = input("You: ")


    if usermessage.lower().strip() in ["bye", "exit", "quit"]:
        print("Bot: Bye! It was nice talking to you.")
        break
      
    response = get_response(usermessage)
    print("Bot:", response)
