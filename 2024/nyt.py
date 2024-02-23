import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.nytimes.com/search?query=+")
soup = BeautifulSoup(r.text, features="html.parser")

items = soup.select("h4")

for i in items:
	print(i.text)