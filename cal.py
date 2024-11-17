height = float(input("What is your height in m:   "))
weight = float(input("What is your weight in kg:  "))

bmi = round(weight / height ** 2)

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight. ")
elif 18.5 <= bmi < 24.9:
    print(f"Your BMI is {bmi}, you have a normal weight. ")
elif 25 <= bmi < 29.9:
    print(f"Your BMI is {bmi}, you are overweight." )
else:
    print(f"Your BMI is {bmi}, you are obese. ")
