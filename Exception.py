# How to use exceptions to handle errors
# Exceptions are used to handle errors in a program
# We just trynna catch errors it's no big deal:-)


try:
    name = input("Kindly what is your name? ")
    age = int(input("Please Enter Your Age: "))
    Annual_income = int(input(f"What's your Annual income {name}? "))
    work_time = int(input("How many months do you work in a year? "))
    monthly_income = Annual_income/work_time
    print(f'Your age is {age} {name} and you earn {monthly_income} per month')
except ValueError:
    print("Please enter a valid Entry")
except ZeroDivisionError:
    print("You cannot divide a number by 0")