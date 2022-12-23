#dictionaries {}
user_message = input("Write something: ")
words = user_message.split(" ")
emojis = {
    ":)":  "🙂",
    ":(": "🙁"
}

output = ""
for word in words:
    output += emojis.get(word, word) + " "

print(output)