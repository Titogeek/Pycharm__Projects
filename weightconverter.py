# Converts weight from KGs to Pounds and VV


weight = input('Enter your weight: ')
choice = input('Is your age in Pounds(l) or Kilograms(k)?: ')
if choice.upper() == 'l':
    kilograms = int(weight)*0.45
    print(f'Your weight in KGs is {kilograms}')
elif choice.upper() == 'K':
    pounds = int(weight)/0.45
    print(f'Your weight in Pounds is {pounds}')
else:
    print("Did we get it right?")

