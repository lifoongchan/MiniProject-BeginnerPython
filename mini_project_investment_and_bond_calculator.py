import math

message = """
investment - calculate the amount of interest you'll earn on your investment 
bond - calculate the amount you'll have to pay on a home loan

Enter either "Investment" or "Bond" from the menu above to proceed:
"""

while True:
    calculator_type = input(f"{message} ").title()
    if calculator_type == "Investment":
        #request input from user for the deposit amount
        deposit = input("\nEnter total amounts of the deposit: ")
        p = float(deposit)

        #request interest rate from user
        interest_rate = input("\nEnter interest rate(%): ")
        r = float(interest_rate)/100

        # request numbers of years on investing
        investment_year = input("\nEnter the numbers of years you are planning on investing: ")
        t = float(investment_year)

        # resquest "simple" or "compound" interest in a varaible called interest 
        interest = input("\nEnter your choice of interest - Simple or Compound:").title()

        if interest == "Simple":
            # Simple interest
            A = p*(1 + r*t)
            A = round(A, 2)
            print(f"The amount you will earn is {A}.")

        
        elif:
            # Compound interest 
            A = p*math.pow((1+r),t)
            A = round(A, 2)
            print(f"The amount you will earn is {A}.")
        
    
    elif calculator_type == "Bond":
        # request  present value of the house
        house_value = input("\nEnter the present value of the house: ")
        P = float(house_value)

        # request the interest rate 
        interest_rate = input("\nEnter the monthly interest rate(%): ")
        interest_rate = (float(interest_rate)/100)
        i = interest_rate/12

        # number of months they plan to take to repay the bond
        months_repay = input("\nEnter the total number of months you plan to repay the bond: \n")
        n = float(months_repay)

        # Bond repayment formula
        repayment = (i * P)/(1 + i)**(-n)
        repayment = round(repayment, 2)
        
        print(f"Money you have to repay each month is {repayment}.")
    
    elif calculator_type == "Quit":
        break
    
    else:
        print("Please enter a valid input")
        continue