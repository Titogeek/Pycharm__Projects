# Emoji converter function
# Use :-) or :-( after text or conversion to emoji

def user_message(message):
    words = message.split(' ')
    emoji = {
        ":-)": "😊",
        ":-(": "😑"
    }
    output = ""
    for word in words:
        output += emoji.get(word, word) + " "

    return output


message = input("Hi there, How are you doing? ")
print(user_message(message))
