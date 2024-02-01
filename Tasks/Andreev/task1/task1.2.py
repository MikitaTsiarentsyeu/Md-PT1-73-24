#Write a program that calculates the area of a circle given its radius, ask a user for the radius.
import math
radius = float(input("Введите радиус круга: \n"))
area = math.pi * radius ** 2
print("Площадь круга равна: ", area)