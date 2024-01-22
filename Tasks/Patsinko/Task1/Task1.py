import math
from decimal import Decimal as D
from random import randint
"1.Write a program that converts Celsius to Fahrenheit, ask a user for the Celsius value."
Cel = float(input('Enter the value in Celsius - '))
print(f'Fahrenheit = {Cel * 1.8 + 32}')

"2.Write a program that calculates the area of a circle given its radius, ask a user for the radius."
radius = float(input('Enter radius value - '))
area_circle = math.pi * radius
print(f'The area of a circle = {round(area_circle, 1)}')

"3.Write a program that converts kilometers per hour to meters per second, ask a user for the speed."
speed_km_h = float(input('Enter speed in kilometers per hour - '))
print(f'Speed in meters per second = {round(speed_km_h / 3.6, 1)}')

'4.Write a program that converts some amount of money from USD to BYN, ask a user for the amount, store the ratio inside the program itself.'
usd = float(input('Enter the amount in USD - '))
print(f'Amount in BYN = {round(D(usd * 3.1707), 2)}')

"5.Write a program that generates a random number in a given range, and shows the answer to a user, ask a user for the left and right border."
range_left = int(input('Enter left border - '))
range_right = int(input('Enter right border - '))
print(f'Random number = {randint(range_left, range_right)}')