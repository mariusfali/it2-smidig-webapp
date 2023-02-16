import requests
from bs4 import BeautifulSoup, SoupStrainer
import time

URL = 'https://www.nrk.no/'

page = requests.get(URL)

soup = BeautifulSoup(page.content,"html.parser")

results = soup.find(class_="kur-house")
#print(results)
#titler = results.find_all("div", class_="articles")
links = results.find_all("a")
#links = results.find_all("a", class_="article")
#print(titler)

#for link in links:
#    print(link)

def sjekk_alle_artikler(ord):
    totalt_poeng = 0
    for link in soup.find_all('a', href=True):
        #print(link)
        totalt_i_artikkel = 0
        ny_url = link['href']
        if ny_url[0] != "#":
            try:
                page1 = requests.get(ny_url)

                soup1 = BeautifulSoup(page1.content,"html.parser")

                antall = soup1.find_all("p")

                for paragraf in antall:
                    tekst = paragraf.text
                    tekst = tekst.lower()
                    resultat = tekst.count(ord.lower())
                    totalt_i_artikkel += resultat
                totalt_poeng += totalt_i_artikkel
            except:
                pass

    return totalt_poeng

#print(sjekk_alle_artikler("Olga Skabejeva"))
    

# ny_url = "https://www.nrk.no/sport/ordkrig-med-ioc-etter-fourcade-intervju_-_-det-heng-ikkje-pa-greip-1.16294017"
# page1 = requests.get(ny_url)

# soup1 = BeautifulSoup(page1.content,"html.parser")

# antall = soup1.find_all("p")

# for paragraf in antall:
#     tekst = paragraf.text
#     resultat = tekst.count("a")
#     totalt_i_artikkel += resultat
    
