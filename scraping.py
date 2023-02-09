import requests
from bs4 import BeautifulSoup

URL = 'https://www.vg.no/'
page = requests.get(URL)

soup = BeautifulSoup(page.content,"html.parser")

results = soup.find(class_="app")
#print(results)
#titler = results.find_all("div", class_="articles")
titler = results.find_all("h2", class_="headline")
#print(titler)
for title in titler:
    kul = title.text
    lower = kul.lower()
    #print(lower)
    if "to" in lower:
        print(lower)