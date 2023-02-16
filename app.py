from flask import Flask, render_template, request, redirect
from scraping import scrape_word
from scraping2 import sjekk_alle_artikler
import json

app = Flask(__name__)


fil = open("politikere.json", encoding="utf-8")
politikere = json.load(fil)
fil.close()

#print(politikere["representanter_oversikt"]["representanter_liste"]["representant"][0]["fornavn"] + politikere["representanter_oversikt"]["representanter_liste"]["representant"][0]["etternavn"])
alle_politikere = []
for i in politikere["representanter_oversikt"]["representanter_liste"]["representant"]:
    #print(i["fornavn"])
    alle_politikere.append(f'{i["fornavn"]} {i["etternavn"]}')


fantasy_lag = []

#print(alle_politikere)


@app.route("/")
def index():
    navn = "Sandvika"
    return render_template("index.html", navn=navn)

@app.route("/results", methods=['POST','GET'])
def results_page():
    #if request.method == 'POST':
    #    word = request.form.get("word")
    #    results = scrape_word(word)
    if request.method == 'POST':
        ord = request.form.get("word")
        results = sjekk_alle_artikler(ord)
    return render_template("index.html", results=results)

@app.route("/lag")
def lag_page():
    return render_template("lag.html", fantasy_lag=fantasy_lag, alle_politikere=alle_politikere)

@app.route("/legg-til-politiker", methods=['POST','GET'])
def legg_til_politiker_funksjon():
    if request.method == 'POST':
        politiker = request.form.get("politiker")
        if len(fantasy_lag) < 8:
            fantasy_lag.append(politiker)
            return render_template("lag.html", fantasy_lag=fantasy_lag, alle_politikere=alle_politikere)
        else:
            return render_template("lag.html", fantasy_lag=fantasy_lag, alle_politikere=alle_politikere)
        
@app.route("/fjern-politiker/<int:id>", methods=['POST','GET'])
def fjern_politiker_funksjon(id):
    if request.method == 'POST':
        fantasy_lag.pop(id-1)
    return render_template("lag.html", fantasy_lag=fantasy_lag, alle_politikere=alle_politikere)
        

app.run(debug=True)