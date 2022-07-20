is_cold=False
is_warm=False

if is_cold:
    print("Wear Warm Clothes")
elif is_warm:
    print('Drink plenty of water')
else:
    print("Get up and grind")
#Exercise
price= 1000000
good_credit=True
#bad_credit=False
if good_credit:
    print("Congratulations, 10% deposit required")
    print(type(price))
    down_payment = (int(price) * 0.1)
    print(f'Down payment is ${down_payment}')

else:
    print("20% deposit required")
    print(int(price) * 0.2)
print("Enjoy your day")

#Comparison
Temperature = 30

if Temperature>=30:
    print("It's a very hot day")
else:
    print("They lied to us")

#Exercise
name=input("What is your name? ")
if len(name)<3:
    print("Name must be atleast 3 characters")
elif len(name)>50:
    print("Name can be a maximum of 50 characters")
else:
    print("Your name has been registered successfully")