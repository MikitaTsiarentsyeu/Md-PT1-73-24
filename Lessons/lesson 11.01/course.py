from urllib.request import urlopen
from bs4 import BeautifulSoup

response = urlopen("https://kurs.onliner.by/")
soup = BeautifulSoup(response, features="html.parser")
tag_list = soup.find_all('p', {'class': 'value fall'})
print(tag_list[0].text, tag_list[1].text)

with open("test.csv", "w") as f:
    f.write(f"{tag_list[0].text},{tag_list[1].text}")