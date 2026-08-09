Task 1 - Rule-Based Chatbot
About the Project
This project is a simple rule-based chatbot created using Python.

The chitchat interacts with the user through the terminal and provides responses based on keywords found in the user's message. It does not use machine learning or any external AI API. Instead, it uses conditional statements and predefined rules to decide how to respond.

I created this project to understand how basic chatbot logic works using Python.

Features
Responds to common greetings such as hello, hi, and hey
Responds to questions like "How are you?"
Tells the user its name and purpose
Provides information about the President of India
Provides information about the Chief Minister of Tamil Nadu
Displays the current time
Displays today's date
Explains what the chatbot can do
Responds to thank-you messages
Gives a supportive response to simple emotional messages
Provides a default response when it does not recognize a question
Allows the user to exit by typing bye, exit, or quit
Technologies Used
Python
datetime module
Conditional statements
Functions
String handling
Loops
User input
How It Works
The chatbot follows a simple process:

The user enters a message.
The message is converted into lowercase and extra spaces are removed.
The chatbot checks the message for specific keywords.
Based on the matching keyword, a suitable response is returned.
The conversation continues until the user types bye, exit, or quit.
For example:

User: hello Bot: Hello! Nice to meet you. How can I help you?

User: what is the time? Bot: The current time is ...

User: what is your name? Bot: I'm a simple rule-based chatbot created using Python.

What I Learned
Through this project, I learned how to:

Create and use functions in Python
Take input from users
Use if, elif, and else conditions
Work with strings and keywords
Use loops to keep a program running
Use the datetime module
Build a simple rule-based conversation system
Conclusion
This project helped me understand the basic logic behind a rule-based chatbot. Although the chatbot works with predefined rules and does not understand language like an AI model, it demonstrates how user input can be processed and connected to different responses using Python.
