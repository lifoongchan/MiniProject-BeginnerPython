number_year = int(input("How many years do you want to check? "))
year = ""
input_count = 0

while input_count < number_year:
    year = int(input("What year do you want to check with? "))

    if year % 4 == 0 and year % 100 == 0:
        print(f"{year} is a leap year")
        input_count +=1
    
    elif year % 4 == 0 and year % 400 == 0:
        print(f"{year} is a leap year")
        input_count +=1

    else:
        print(f"{year} isn't a leap year")
        input_count +=1
