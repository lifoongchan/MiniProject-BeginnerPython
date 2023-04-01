#dictionaries {}
phone_num = input("Key in a phone number: ")
word = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"

}

for digit in phone_num:
    print(word.get(digit,"Invalid Number"))
