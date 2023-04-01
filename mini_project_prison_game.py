# 1 = a free cell
# 0 = a locked cell

# change 0 to 1; change 1 to 0
prison = [1, 1, 1, 1, 1, 1, 1]
not_free = True
freed_prisoner = 0

print(prison)

while freed_prisoner < 7:
  cell = int(input("Enter cell you want to free: "))
  if cell == 7:
    print("\nGame Over. Start again!\n")
    break  
  
  elif cell == 1:
    prison [2] = 0
    prison [3] = 0
    prison [4] = 0
    prison [6] = 0
    prison [0] = 1
    prison [1] = 1
    prison [5] = 1
    freed_prisoner +=4
    print(f"\n {prison}\n You freed 4")
    new_cell = int(input("Enter cell you want to free: "))

    if new_cell == 3:
      prison [2] = 1
      prison [3] = 1
      prison [4] = 1
      prison [6] = 1
      prison [0] = 0
      prison [1] = 0
      prison [5] = 0
      freed_prisoner +=3
      print(f"\n {prison}\n You freed {freed_prisoner} in total.")
      not_free = False
      break
    
    elif new_cell == 7:
      print("\nGame Over. Start again!\n")
      break
    
    else:
      print("Try Again.")
      pass
  
  elif cell == 6:
    prison [2] = 0
    prison [3] = 0
    prison [4] = 0
    prison [6] = 0
    prison [0] = 1
    prison [1] = 1
    prison [5] = 1
    freed_prisoner +=4
    print(f"\n{prison}\n You freed 4")
    new_cell = int(input("Enter cell you want to free: "))

    if new_cell == 3:
      prison [2] = 1
      prison [3] = 1
      prison [4] = 1
      prison [6] = 1
      prison [0] = 0
      prison [1] = 0
      prison [5] = 0
      freed_prisoner +=3
      print(f"\n{prison}\n You freed {freed_prisoner} in total.\n")
      not_free = False
      break
    
    elif new_cell == 7:
      print("\nGame Over. Start again!\n")
      break
    
    else:
      print("Try Again.")
      pass
  
  elif cell == 3:
    prison [2] = 1
    prison [3] = 1
    prison [4] = 1
    prison [6] = 1
    prison [0] = 0
    prison [1] = 0
    prison [5] = 0
    freed_prisoner +=3   
    print(f"\n{prison}\n You freed {freed_prisoner}")
    more_cell = int(input("Enter cell you want to free: "))
    
    if more_cell == 1:
      prison [2] = 0
      prison [3] = 0
      prison [4] = 0
      prison [6] = 0
      prison [0] = 1
      prison [1] = 1
      prison [5] = 1
      freed_prisoner +=4
      print(f"\n{prison}\n You freed {freed_prisoner}. You won!")
      not_free = False
      break
      
    elif more_cell == 6:
      prison [2] = 0
      prison [3] = 0
      prison [4] = 0
      prison [6] = 0
      prison [0] = 1
      prison [1] = 1
      prison [5] = 1
      freed_prisoner +=4
      print(f"\n{prison}\n You freed {freed_prisoner}. You won!")
      not_free = False
      break
      
    elif more_cell == 7:
      print("Game Over. Start again!")
      break
    
    else:  
      print("Try Again.")
      pass
  
  else:
    print(f"\n{prison}\nRemained locked :/ \n")
    pass
  
