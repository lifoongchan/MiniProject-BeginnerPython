n = ""
total_number = 0
time_input = 0

while n != -1:
    n = int(input("Enter a number: "))
    total_number += n
    time_input += 1

formula = total_number/time_input
print (f"The average of the numbers you have enter is {round(formula, 2)}")