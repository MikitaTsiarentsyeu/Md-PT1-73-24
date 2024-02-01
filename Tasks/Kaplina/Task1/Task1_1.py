#1.Write a program that converts Celsius to Fahrenheit, ask a user for the Celsius value.

import math

temp_Celsius = int(input("Please, enter the temperature in Celsium\n"))
temp_Fahrenheit = round((temp_Celsius * 9 / 5) + 32)
print("The temperature is", temp_Fahrenheit, "°F")