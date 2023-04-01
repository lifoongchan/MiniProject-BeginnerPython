# calculate the cost of sending a parcel

#request the price of the item 
#request total distance of the delivery in kms

item_price = float(input("\nEnter price of the item: "))

total_distance = float(input("\nEnter distance of the delivery in km: "))

delivery_method = input("\nEnter delivery method - (A)Air or (F)Freight: ").upper()
air_cost = 0.35
freight_cost = 0.25
total_air_cost = air_cost*total_distance
total_freight_cost = freight_cost* total_distance

gift = input("\nGift(Y) or no gift(N): ").upper()
is_gift = 15.00
no_gift = 0.00

insurance = input("\nFull insurance(F) or limited insurance(L): ").upper
full_price = 50.00
partial_price = 25.00

priority = input("\nPriority(P) or standard(S) delivery: ").upper
priority_price = 100.00
standard_price = 20.00


if  delivery_method == "A" and gift == "Y":
    total_cost = total_air_cost + is_gift
    
    if insurance == "F" and priority == "P":
        total_cost += full_price + priority_price
        print(f"Your final cost is {round(total_cost, 2)}")
   
    elif insurance =="F" and priority == "S":
        total_cost += full_price + standard_price
        print(f"Your final cost is {round(total_cost, 2)}")

    elif insurance =="L" and priority == "P":
        total_cost += partial_price + priority_price
        print(f"Your final cost is {round(total_cost, 2)}")

    else:
        total_cost += partial_price + standard_price
        print(f"Your final cost is {round(total_cost, 2)}")

elif delivery_method == "A" and gift == "N":
   
    total_cost = total_air_cost + no_gift
    
    if insurance == "F" and priority == "P":
        total_cost += full_price + priority_price
        print(f"Your final cost is {round(total_cost, 2)}")
   
    elif insurance =="F" and priority == "S":
        total_cost += full_price + standard_price
        print(f"Your final cost is {round(total_cost, 2)}")

    elif insurance =="L" and priority == "P":
        total_cost += partial_price + priority_price
        print(f"Your final cost is {round(total_cost, 2)}")

    else:
        total_cost += partial_price + standard_price
        print(f"Your final cost is {round(total_cost, 2)}")


elif delivery_method == "F" and gift == "Y":
    
    total_cost = total_freight_cost + is_gift
    
    if insurance == "F" and priority == "P":
        total_cost += full_price + priority_price
        print(f"Your final cost is {round(total_cost, 2)}")
   
    elif insurance =="F" and priority == "S":
        total_cost += full_price + standard_price
        print(f"Your final cost is {round(total_cost, 2)}")

    elif insurance =="L" and priority == "P":
        total_cost += partial_price + priority_price
        print(f"Your final cost is {round(total_cost, 2)}")

    else:
        total_cost += partial_price + standard_price
        print(f"Your final cost is {round(total_cost, 2)}")


else:
    
    total_cost = total_freight_cost + no_gift

    if insurance == "F" and priority == "P":
        total_cost += full_price + priority_price
        print(f"Your final cost is {round(total_cost, 2)}")
   
    elif insurance =="F" and priority == "S":
        total_cost += full_price + standard_price
        print(f"Your final cost is {round(total_cost, 2)}")

    elif insurance =="L" and priority == "P":
        total_cost += partial_price + priority_price
        print(f"Your final cost is {round(total_cost, 2)}")

    else:
        total_cost += partial_price + standard_price
        print(f"Your final cost is {round(total_cost, 2)}")
