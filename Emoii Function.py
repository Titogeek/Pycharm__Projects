# Emoji converter function
# Use :-) or :-( after text or conversion to emoji
message = input("Hi there, How are you doing? ")


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


print(user_message(message))