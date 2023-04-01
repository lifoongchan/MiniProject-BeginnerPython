username = len(input("Enter your username: "))

if username < 3:
    print("username must be at least 3 characters")

elif username > 50:
    print("username can be a maximum of 50 characters")

else:
    print("your username looks great :>")
