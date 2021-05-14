import random
# Angela, Simon, Carol, Zachary, Storm, Philip, Levi
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
print(f"{random.choice(names)} is paying the bill")