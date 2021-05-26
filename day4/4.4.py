import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choices = [rock, paper, scissors]

user = input("Choose 0 for rock, 1 for paper and 2 for scissors: ")
userInput = int(user)
print(choices[userInput])
compInput = random.randint(0, 2)
print(f"Computer picks {compInput}")
print(choices[compInput])

if userInput == 0:
    if compInput == 0:
        print("Draw")
    elif compInput == 1:
        print("Lose")
    else:
        print ("Win")
elif userInput == 1:
    if compInput == 0:
        print("Win")
    elif compInput == 1:
        print("Draw")
    else:
        print ("Lose")
elif userInput == 2:
    if compInput == 0:
        print("Lose")
    elif compInput == 1:
        print("Win")
    else:
        print ("Draw")
