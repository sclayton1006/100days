valueInput = (int(input("Enter the value you wish to check: ")))
calculate = valueInput % 2
if calculate == 0:
    print(f"{valueInput} is an even number.")
else:
    print(f"{valueInput} is an odd number.")
