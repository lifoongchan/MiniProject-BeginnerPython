user=input("What is your name? Answer: ")
print(f"\nWelcome to your personal BMI Calculator, {user}!\n")

w=float(input("Weight in kilograms: "))
h=float(input("Height in meters: "))

BMI=w/(h*h)
newBMI=round(BMI,2)

print(f"Your BMI is {str(newBMI)}")

if newBMI<=18.5: 
       print(f"You're in the underweight. Eat some foods and gain more weight, {user} :C")
    
elif newBMI<=24.5:
       print(f"Well done, {user}, you're in the healthy weight range :D")

elif newBMI<=29.9:
       print(f"{user}, you're in the overweight range. Do some exercising would help :C")

else:
       print(f"{user}, you're in the obese range. Try balancing your diet :C")
