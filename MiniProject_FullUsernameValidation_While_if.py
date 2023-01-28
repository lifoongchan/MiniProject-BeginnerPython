full_name = ""
is_validated = False

while is_validated == False:
    full_name = input("Enter your full name: ")

    #use len() to calculate the character count
    no_space_name = full_name.replace(" ", "")
    character_count = len(no_space_name)

    #use split and calculate word count
    word_list = full_name.split()
    word_count = len(word_list)
    
    if word_count >= 2:
        if character_count <4:
            print("You have entered less than 4 characters, please make sure that you have enter your full name." )
        
        elif character_count >25:
            print("You have entered more than 25 characters. Please make sure that you have only entered your full name.")
    
        else:
            is_validated = True
            print("Thank you for entering your name.")
            break

    elif word_count == 1:
        print("Please make sure that you have entered your full name.")
    
    else:
        print("You haven't entered anything. Please enter your full name.")


