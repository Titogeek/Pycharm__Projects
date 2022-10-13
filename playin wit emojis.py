#Giving user output with smiley emoji

message = input("What's The Message For Her Brother ")
words = message.split(' ')
emoji = {
    ":-)": "😊",
    ":-(": "😑"
}
output = ""
for word in words:
    output += emoji.get(word, word) + " "

print(output)




