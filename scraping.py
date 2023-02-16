import requests
from bs4 import BeautifulSoup, SoupStrainer
import time

URL = 'https://www.vg.no/'

page = requests.get(URL)

soup = BeautifulSoup(page.content,"html.parser")

results = soup.find(class_="app")
#print(results)
#titler = results.find_all("div", class_="articles")
titler = results.find_all("h2", class_="headline")
#links = results.find_all("a", class_="article")
#print(titler)
for title in titler:
    kul = title.text
    lower = kul.lower()
    #print(lower)
    #if "to" in lower:
    #    print(lower)

def scrape_word(word):
    poeng = 0
    for title in titler:
        tekst = title.text
        lower = tekst.lower()
        if word.lower() in lower:
            poeng += 1
    return poeng

def scrape_all_articles_for_word(word):
    poeng = 0



#time.sleep(0.1) kan ha med randint for 0.1 der