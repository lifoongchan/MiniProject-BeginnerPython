secret_number = 25
guess_count = 0 #the number of guesses user has mad
guess_limit = 5

while guess_count < guess_limit: #execute 5 times
    guess = int(input("Guess a number: "))
    guess_count +=1
    if guess == secret_number:
        print("Yay, you got it!")
        break #terminate the loop

    elif guess < secret_number:
        print("Try it again. Too low :/")

    elif guess > secret_number:
        print("Try it again. It's too high :/")
else:
    print("You've ran out your chances :<")
#else is on the same line as while meaning that when it reaches the guess limit,
#it will print the things after else