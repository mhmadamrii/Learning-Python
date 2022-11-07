import random

greetings = ["Hello", "What's up", "Howdy", "Greetings"]
goodbyes = ["Bye", "Goodbye", "See you later", "See you soon"]

keywords = ["music", "pet", "book", "game"]
responses = ["Music is so relaxing!", "Dogs are man's best friend", "I know about a lot  of books.", "I like to play  video game"]

print(random.choice(greetings))

user = input("Say somethig(or type bye to quit)")
user = user.lower()

while(user != "bye"):
    for index in range(len(keywords)):
        if(keywords[index] in user):
            print("Bot: " + responses[index])