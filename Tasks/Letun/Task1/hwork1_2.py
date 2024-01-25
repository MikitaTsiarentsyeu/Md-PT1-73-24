#2.Write a program that calculates the area of a circle given its radius, ask a user for the radius.

from math import pi
r = float(input("Input the radius of the circle : "))
area = pi * r ** 2
print("The area of the circle with radius" + str(r) + " is: " + str(area))