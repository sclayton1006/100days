print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()
name3 = name1 + name2

value1 = 0
value2 = 0

value1 += name3.count("t")
value1 += name3.count("r")
value1 += name3.count("u")
value1 += name3.count("e")
value2 += name3.count("l")
value2 += name3.count("o")
value2 += name3.count("v")
value2 += name3.count("e")

bounce = f"{value1}{value2}"
value3 = int(bounce)

if value3 < 10 or value3 > 90:
    print(f"Your score is {value3}, you go together like \
coke and mentos.")
elif value3 > 40 and value3 < 50:
    print(f"Your score is {value3}, you are alright \
together.")
else:
    print(f"Your score is {value3}.")