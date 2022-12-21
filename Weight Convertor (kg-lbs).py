w = float(input("Enter your weight: "))
u = input("(L)bs or (K)g: ").upper()
x = 0.45359237

if u == "L":
     print(f"your weight in kg is {round(w*x,2)}")

if u == "K":
     print(f"your weight in lbs is {round(w/x,2)}")