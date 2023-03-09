height = float(input("What is your height in meters ?\n"))
weight = float(input("What is your weight in kilos ?\n"))

bmi = weight / height ** 2

if bmi < 18.5:
    print("You are underweight")
elif bmi >= 18.5 and bmi < 25:
    print("You have a normal weight")
elif bmi >= 25 and bmi < 30:
    print("You are slightly overweight")
elif bmi >= 30 and bmi < 35:
    print("You are obese")
elif bmi >= 35 :
    print("You are clinically obese")