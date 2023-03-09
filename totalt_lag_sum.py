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

def sjekk_team_score(lag):
    total_score = 0
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
                    for politiker in lag:
                        resultat = tekst.count(politiker.lower())
                        totalt_i_artikkel += resultat
                total_score += totalt_i_artikkel
            except:
                pass

    return total_score