def main():
    print("\nThis program covert US Dollars to Pounds Sterling.")

    dollars = eval(input("Enter amount in dollars: $ "))

    pounds = dollars * 0.82

    pounds = round(pounds, 2)

    print(f"\nNew amount: £{pounds}")


while True:
    command = input("\nStart converting (yes/no): ")
    if command.lower() == "yes":
        main()

    elif command.lower() == "no":
        quit()

    else:
        print("Typing Error. Please check and try again.")
