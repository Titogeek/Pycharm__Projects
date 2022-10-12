#printing x,y coordinates
#program will run until inner loop is complete >> 0 >> range 6
#The proceeds to the second iteration of the outter loop
for coordinate_x in range(4):
    for coordinate_y in range(4):
        print(f'{coordinate_x}, {coordinate_y}')


#Challenge
number_v= [5,2,5,2,2]
for numbers in number_v:
    output = ''
    for count in range(numbers):
        output += 'x'
    print(output)

