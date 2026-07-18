##Task 1 - Rule-Based Chatbot

#About the Project

This project is a simple rule-based chatbot created using Python.

The chitchat interacts with the user through the terminal and provides responses based on keywords found in the user's message. It does not use machine learning or any external AI API. Instead, it uses conditional statements and predefined rules to decide how to respond.

I created this project to understand how basic chatbot logic works using Python.

## Features

1. Responds to common greetings such as hello, hi, and hey
2. Responds to questions like "How are you?"
3. Tells the user its name and purpose
4. Provides information about the President of India
5. Provides information about the Chief Minister of Tamil Nadu
6. Displays the current time
7. Displays today's date
8. Explains what the chatbot can do
9. Responds to thank-you messages
10. Gives a supportive response to simple emotional messages
11. Provides a default response when it does not recognize a question
12. Allows the user to exit by typing bye, exit, or quit

## Technologies Used

1. Python
2. datetime module
3. Conditional statements
4. Functions
5. String handling
6. Loops
7. User input

## How It Works

The chatbot follows a simple process:

1. The user enters a message.
2. The message is converted into lowercase and extra spaces are removed.
3. The chatbot checks the message for specific keywords.
4. Based on the matching keyword, a suitable response is returned.
5. The conversation continues until the user types `bye`, `exit`, or `quit`.

For example:

User: hello
Bot: Hello! Nice to meet you. How can I help you?

User: what is the time?
Bot: The current time is ...

User: what is your name?
Bot: I'm a simple rule-based chatbot created using Python.


## What I Learned

Through this project, I learned how to:

* Create and use functions in Python
* Take input from users
* Use `if`, `elif`, and `else` conditions
* Work with strings and keywords
* Use loops to keep a program running
* Use the `datetime` module
* Build a simple rule-based conversation system

## Conclusion

This project helped me understand the basic logic behind a rule-based chatbot. Although the chatbot works with predefined rules and does not understand language like an AI model, it demonstrates how user input can be processed and connected to different responses using Python.
