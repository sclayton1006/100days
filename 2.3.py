print(
    "This program will tell you how many \n\
days months and years you have left to \n\
90 years old.\n")
userInput = input("What is your current age? ")

daysLeft = ((90*365)-int(userInput)*365)
weeksLeft = ((90*52)-int(userInput)*52)
monthsLeft = ((90*12)-int(userInput)*12)

print(f"You have {daysLeft} days, or {weeksLeft} weeks, or {monthsLeft} months until you are 90.")
