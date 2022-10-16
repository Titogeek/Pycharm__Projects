# Converts weight from KGs to Pounds and VV


def user_input():
    name = input("Hi There, Please Enter Your Name To Use The Weight Converter Application: ")
    weight = input('Enter your weight: ')
    choice = input('Is your age in Pounds(l) or Kilograms(k)?: ')
    if choice.upper() == 'l':
        kilograms = int(weight)*0.45
        print(f'Your weight in KGs is {kilograms} {name}')
    elif choice.upper() == 'K':
        pounds = int(weight)/0.45
        print(f'Your weight in Pounds is {pounds} {name}')
    else:
        print("Did we get it right?")

