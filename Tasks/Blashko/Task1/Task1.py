from math import pi
import requests
from bs4 import BeautifulSoup
from decimal import Decimal
from random import randint


"""1.Write a program that converts Celsius
 to Fahrenheit, ask a user for the Celsius value."""

celsius = float(input("Please enter Celsius value: "))
fahrenheit = (celsius * 9) / 5 + 32
print(fahrenheit)


"""2.Write a program that calculates the area of 
a circle given its radius, ask a user for the radius."""

radius = float(input("Please enter radius value: "))
area = pi * radius ** 2
print(area)


"""3.Write a program that converts kilometers per 
hour to meters per second, ask a user for the speed."""

speed = float(input("Please enter speed: "))
met_per_sec = speed * 10 / 36
print(round(met_per_sec, 3))


"""4.Write a program that converts some amount of money 
from USD to BYN, ask a user for the amount, store the 
ratio inside the program itself."""

usd = int(input("Please enter value in usd: "))

response = requests.get('https://myfin.by/currency/usd')
bs = BeautifulSoup(response.text, "html.parser")
byn = bs.find_all("span", {"class": "accent"})[1].text

exchange = Decimal(byn) * usd
print(exchange)


"""5.Write a program that generates a random number 
in a given range, and shows the answer to a user, ask
 a user for the left and right border."""

a, b = map(int, input("Enter first and second value separated by a space : ").split())
print(f"You random number is:  {randint(a, b)}")
