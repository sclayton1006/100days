print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()
name3 = name1 + name2

value = 0

value += name3.count("t")
value += name3.count("r")
value += name3.count("u")
value += name3.count("e")
value += name3.count("l")
value += name3.count("o")
value += name3.count("v")
value += name3.count("e")

if value < 10 or value > 90:
    print(f"Your score is {value}, you go together like \
coke and mentos.")
elif value > 40 and value < 50:
    print(f"Your score is {value}, you are alright \
together.")
else:
    print(f"Your score is {value}.")