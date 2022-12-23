user=input("Enter your name: ")
print("\n")
print(f"Welcome to Shiba Land, {user}! :D You have encountered Shiba the Conqueror!\
\nShiba: Meow! No entry! You need to pay 300 cookies to enter Shiba Land legally :<\n")

print("\n")
cookies=int(input("Enter the cookie amount you would pay: "))

if cookies<300: 
    print("Shiba: This is not enough! Meow! You're permanently banned from Shiba Land!")

elif cookies<500:
    print("Shiba:This is satisfactory. You're paying the bare minimum, meow. Follow Shiba :<")

else:
    print("Shiba: Shiba approooves, meow meow :3 Come with Shiba :3")
