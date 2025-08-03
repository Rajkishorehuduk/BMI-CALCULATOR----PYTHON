
height = float(input("Enter your height in feet (e.g., 1.75): "))
weight = float(input("Enter your weight in kilograms (e.g., 68): "))

bmi = weight / (height ** 2)

print(f"Your BMI is: {bmi:.2f}")

if bmi < 18.5:
    print("You are underweight.")
elif bmi < 25:
    print("You have a normal weight.")
elif bmi < 30:
    print("You are overweight.")
    
else:
    print("You are obese.")
