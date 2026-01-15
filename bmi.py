# BMI calculator
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))
bmi = weight / (height ** 2)
print(f"Your BMI is: {bmi:.2f}")

# BMI Classification
if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal weight"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

print(f"Category: {category}")