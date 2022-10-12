#unpacking items in a tuple into a variable
#unpacking is not limited to tuples only---lists,,,
coordinates = (3, 4, 6)
x, y, z = coordinates
print(x,y,z)

#Dictionaries- Sorry had to include this in tuples file
#We just playing outhere

Admin_data ={
    "Name": "Annabelle Murigi",
    "School": "School Of Arts",
    "Age": 21,
    "Religion": "Pagan"
}
print(Admin_data.get("Name"))

#Exersise

phone_number = input("Enter Your Phone Number: ")
print(type(phone_number))
numbers_diction = {
    "1": " One ",
    "2": " Two ",
    "3": " Three ",
    "4": " Four ",
    "5": " Five ",
}
output= ""
print(numbers_diction["1"])
for items in phone_number:
    output += numbers_diction.get(items, "!!!")

print(output)

# print(numbers_diction.get("1"))
#
# for key in numbers_diction:





