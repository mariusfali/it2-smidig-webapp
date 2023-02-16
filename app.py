from flask import Flask, render_template, request
from scraping import scrape_word
from scraping2 import sjekk_alle_artikler

app = Flask(__name__)

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
    return render_template("lag.html")

app.run(debug=True)