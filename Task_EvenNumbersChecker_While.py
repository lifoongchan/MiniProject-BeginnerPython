n = int(input("Input a number: ")) #Taking in user input to use as n
    
i = 1 #starts with 1

while i <= n: #loop continues until i becomes more than the input
    if i % 2 == 0: #if the i is devided by 2 and it has no leftover, then print i
        print(i)
    i += 1 #add 1 to i
