# 5.Write a program that generates a random number in a given range, and shows the answer to a user, ask a user for the left and right border.

import math
import random

left_border = int(input("Please, enter the left border for a random number\n"))
right_border = int(input("Please, enter the right border for a random number\n"))
random_number = random.randint(left_border, right_border)
print("Random number in the given range is", random_number)




