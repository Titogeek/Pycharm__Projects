#finding the largest number in a list

numbers = [200,40,4,700,90,300]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)

#Remove duplicates in a list
non_duplicates = list()
for item in numbers:
    if item not in non_duplicates:
        non_duplicates.append(item)
print(non_duplicates)


