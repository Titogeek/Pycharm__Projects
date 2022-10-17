# Playin' wit built-in functions

import random

for i in range(10):
    print(random.random())
    print(random.randint(30, 40))

# Picking a leader randomly from a list

members_list = ['Annabelle', 'Sophie', 'Mercy', 'Valentine', 'Floric']
leader = random.choice(members_list)
print(f"{leader} is the leader of the group")

# Rolling a Die Exercise
# First I think to have a list with 6 numbers - A die has six sides


class Dice:
    def roll(self):
        random_numbers = (1, 2, 3, 4, 5, 6)

        final_roll = ()
        side_one = random.choice(random_numbers)
        side_two = random.choice(random_numbers)

        final_roll = final_roll + (side_one, side_two)
        print(final_roll)


Dice.roll(' ')


