names = ""
total_entered = 0

while names != "Stop":
    names = input("Enter a name: ").title()
    total_entered += 1
    
print(f"Total number of names entered = {total_entered}")