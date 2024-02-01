#2.Write a program that calculates the area of a circle given its radius, ask a user for the radius.

import math

radius = int(input("Please, enter the radius\n"))
area = round(math.pi * radius**2)
print("The area of circle is", area)
