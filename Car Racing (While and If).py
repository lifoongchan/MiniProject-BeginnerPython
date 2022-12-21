command = ""
initial_started = False

while True:
    # while <condition>;
    # != is not equal to
    # if the command is not "quit", loop continues
    # to simplify, use while true meaning if the condition stays until breaks

    command = input("- ").lower()
    if command == "help":
        print('''
        Start - to start the car 
        Stop - to stop the car 
        Faster - to accelerate the car
        Slower - to slower the car
        Quit - to exit''')

    elif command == "start":
          if initial_started:
              #initial_started = false - car is not start
              #in python, initial_started = true/false doesnt work with if  :
              print("Car is already started!")
          else:
              initial_started = True #change initial started to true
              print("Car started! Read to go :>")

    elif command == "stop":
           if not initial_started:
               print("Car is already stopped!")
           else:
               initial_started = False
               print("Car is stopped!")

    elif command == "faster":
        print("Speed increases!")

    elif command == "slower":
        print("Speed decreases!")

    elif command == "quit":
        print("- Game quit -")
        break

    else:
        print("I don't understand what you mean..")
