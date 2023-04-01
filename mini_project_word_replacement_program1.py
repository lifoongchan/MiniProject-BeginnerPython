""" This file is for editing texts """


STARTED = True

while True:
    text = input("Enter a message: ")
    print(text)
    initial_command = input("Do you want to edit the text? - yes or no: ")
    word_to_replace =  input("Enter the word to replace: ")
    word_replacement = input("Enter the word replacement: ")
    final_command = input("Anything else? - replace more or done: ")
    if initial_command.lower() == "no" or final_command.lower() == "done":
        break
    else:
        continue


print(text.replace(word_to_replace, word_replacement))
