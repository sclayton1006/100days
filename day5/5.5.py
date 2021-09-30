#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password? ")) 
nr_symbols = int(input(f"How many symbols would you like? "))
nr_numbers = int(input(f"How many numbers would you like? "))

passwordLst = []

for a in range(1, nr_letters + 1):
    a = random.choice(letters)
    passwordLst.append(a)
for b in range(1, nr_numbers + 1):
    b = random.choice(numbers)
    passwordLst.append(b)
for c in range(1, nr_symbols + 1):
    c = random.choice(symbols)
    passwordLst.append(c)

random.shuffle(passwordLst)
finalAnswer = "".join(passwordLst)

print(f"You random password is: {finalAnswer}")