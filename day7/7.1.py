#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

import random

chosen_word = random.choice(word_list)
guess = input("Guess a random letter: ").lower()

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
