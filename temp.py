from Jarvis_main import *
from bs4 import BeautifulSoup
import requests

search = "Weather in mumbai"
url = f"https://www.google.com/search?&q={search}"
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")
update = soup.find("div", class_="BNeawe").text
print(f"{search} now is {update}")
