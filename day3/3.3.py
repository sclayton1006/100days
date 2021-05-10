year = int(input("Which year do you want to check? "))

divByFour = year % 4
divByHundred = year % 100
divByFourHundred = year % 400
matchTest = divByHundred + divByFourHundred

# On every year that is evenly divisible by 4 **except** 
# every year that is evenly divisible by 100 **unless** 
# the year is also evenly divisible by 400

if matchTest == 0:
    print("Leap!")
elif divByHundred == 0:
    print("Not a leap...")
elif divByFour == 0:
    print("Leap!")
else:
    print("Not a leap...")
