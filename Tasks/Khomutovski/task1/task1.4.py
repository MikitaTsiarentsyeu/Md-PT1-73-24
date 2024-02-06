import requests
from bs4 import BeautifulSoup
from decimal import Decimal


usd = int(input("Please enter value in usd: "))

response = requests.get('https://myfin.by/currency/usd')
bs = BeautifulSoup(response.text, "html.parser")
byn = bs.find_all("span", {"class": "accent"})[1].text

exchange = Decimal(byn) * usd
print(exchange)