#Formatted String
first = 'Titus'
last = 'Kachapin'
msg= f'{first} [{last}] is a coder'
print(first + ' [' + last + '] is a coder')
print(msg)


#finding age
birth_year= input("What's your birth year? ")
print(type(birth_year))
current_year= input("what's the year now? ")
age= int(current_year)-int(birth_year)
print(age)

#getting weight in pound and converting it to kilogram
weight_pound= input("Hello, What is your weight in pounds? ")
#1kg = 2.2 pounds
weight_kg= int(weight_pound)/2.2
print(weight_kg)



