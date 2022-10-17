# module to find the maximum number in a list
# Playing around with packages concept >> Hope we win


def max_number():
    # Creating an empty list
    number_list = []
    number_of_elements = int(input("How many items do you want in your list?: "))
    print("Please enter the items you want in your list below > ")

    # iterating till range
    for nums in range(0, number_of_elements):
        ele = int(input())
        number_list.append(ele)  # adding the element

    print(f'The items in your list are {number_list}')

    max_num = number_list[0]
    for number in number_list:
        if number > max_num:
            max_num = number
    print(f'The Maximum number in your list is {max_num}')



