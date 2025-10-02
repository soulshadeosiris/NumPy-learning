import numpy as np
from collections import Counter

words_hi = ['Hi', 'Hello', 'Hey']
words_hi_array = np.array(words_hi)
how_are_you = ["How are you", "How is it going", "How are you doing"]
how_are_you_array = np.array(how_are_you)
user_doing = ['good', 'bad']

def hi():
    print("Hi! I'm a simple ML model")
    user_input_hi = input()

    if any(word.lower() in user_input_hi.lower() for word in words_hi_array):
        print("Hi! I'm glad to see you here.")

def howAreYou():
    user_input_question_doing = input()

    if any(word.lower() in user_input_question_doing.lower() for word in how_are_you_array):
        print("I'm doing good, and you?")

    user_input_doing = input()

    if user_doing[0].lower() in user_input_doing.lower():
        print("I'm happy to hear that you are good!")
    else:
        print("It makes me hurt to hear that you are sad, bro(")

while True:
    hi()
    howAreYou()