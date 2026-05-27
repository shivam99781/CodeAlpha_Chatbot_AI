print("AI STYLE PYTHON CHATBOT")

print("\nType 'bye' to exit the chatbot.\n")

while True:

    user = input("You: ").lower()

    if user in ["hello", "hi", "hey"]:
        print("Bot: Hello! How can I help you?")

    elif "tell me about yourself" in user or "who are you" in user or "about yourself" in user:
        print("Bot: I am an AI Style Python Chatbot created by Shivam Garg. I can answer basic questions, perform calculations, tell date and time, and chat with users like a virtual assistant.")

    elif "how are you" in user:
        print("Bot: I am fine and ready to help you!")

    elif "your name" in user:
        print("Bot: I am an AI Python Chatbot.")

    elif "who created you" in user:
        print("Bot: I was created by Shivam Garg using Python programming.")

    elif "time" in user:
        import datetime
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print("Bot: Current time is", current_time)

    elif "date" in user:
        import datetime
        current_date = datetime.datetime.now().strftime("%d-%m-%Y")
        print("Bot: Today's date is", current_date)

    elif "python" in user:
        print("Bot: Python is a popular programming language used in AI, ML, Web Development and Data Science.")

    elif "ai" in user or "artificial intelligence" in user:
        print("Bot: Artificial Intelligence helps machines think and solve problems like humans.")

    elif "machine learning" in user:
        print("Bot: Machine Learning is a branch of AI where machines learn from data.")

    elif "college" in user:
        print("Bot: College life is a great time to learn skills and build projects.")

    elif "motivate me" in user:
        print("Bot: Keep learning daily. Small progress every day creates big success.")

    elif "joke" in user:
        print("Bot: Why do programmers prefer dark mode? Because light attracts bugs!")

    elif "skills" in user:
        print("Bot: You should learn Python, DSA, AI/ML and projects for tech internships.")

    elif "internship" in user:
        print("Bot: Internships help you gain real-world experience and improve your resume.")

    elif "weather" in user:
        print("Bot: Sorry, I cannot access live weather data in this offline version.")

    elif "calculate" in user:
        try:
            expression = user.replace("calculate", "")
            result = eval(expression)
            print("Bot: Answer =", result)
        except:
            print("Bot: Invalid calculation.")

    elif user == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't know the answer to that yet.")
