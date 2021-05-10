height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

# BMI calculation is calculated by dividing a person's 
# weight (in kg) by the square of their height (in m):
bmiCalculation = round((weight // (height ** 2)))

#Conditional output based on result:
# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.
if bmiCalculation < 18.5:
    print(f"Your BMI is {bmiCalculation}, which means you are underweight")
elif bmiCalculation < 25:
    print(f"Your BMI is {bmiCalculation}, which means you are normal")
elif bmiCalculation < 30:
    print(f"Your BMI is {bmiCalculation}, which means you are slightly overweight")
elif bmiCalculation < 35:
    print(f"Your BMI is {bmiCalculation}, which means you are obese")
elif bmiCalculation >= 35:
    print(f"Your BMI is {bmiCalculation}, which means you are clinically obese")
