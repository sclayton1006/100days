#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

import random

chosen_word = random.choice(word_list)
guess = input("Guess a random letter: ")

counter = 0
for letter in range(len(chosen_word)):
    if guess == chosen_word[counter]:
        print("Right")
    else:
        print("Wrong")
    counter += 1

