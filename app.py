from flask import Flask, render_template, request, redirect, url_for, flash, session
from scraping import scrape_word
from scraping2 import sjekk_alle_artikler
import json
from totalt_lag_sum import sjekk_team_score

app = Flask(__name__)
app.app_context().push()


# Database pain ----------------------

from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc, func, PickleType, select, and_, exists
from sqlalchemy.ext.mutable import MutableList
from sqlalchemy.dialects.mysql import match
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash

from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
#from flask_wtf.file import FileField
from werkzeug.utils import secure_filename




app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

app.config['SECRET_KEY'] = "super secret key here"

#UPLOAD_FOLDER = 'static/bilder/'
#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

db = SQLAlchemy(app)
#migrate = Migrate(app, db)

# ------------------------------------

# Login stuff -----

# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = 'login'

# @login_manager.user_loader
# def load_user(user_id):
#     return Users.query.get(int(user_id))

# -----------------

# Module ---------

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    #password = db.Column(db.String(200), nullable=False)
    date_added = db.Column(db.DateTime, default=func.now())
    password_hash = db.Column(db.String(128))
    team_value = db.Column(db.Integer)
    team = []

    # @property
    # def password(self):
    #     raise AttributeError("password is not a readable attribute!")

    # @password.setter
    # def password(self, password):
    #     self.password_hash = generate_password_hash(password)

    # def verify_password(self, password):
    #     return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<Username %r>' % self.username
    
# ----------------


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
            return redirect(request.referrer)
        else:
            return redirect(request.referrer)
        
@app.route("/fjern-politiker/<int:id>", methods=['POST','GET'])
def fjern_politiker_funksjon(id):
    if request.method == 'POST':
        fantasy_lag.pop(id-1)
    return redirect(request.referrer)

@app.route("/team-score", methods=['POST','GET'])
def sjekk_lag_score():
    if request.method == 'POST':
        lag_poeng = sjekk_team_score(fantasy_lag)
    return render_template("lag.html", lag_poeng=lag_poeng, fantasy_lag=fantasy_lag, alle_politikere=alle_politikere)
        


        

app.run(debug=True)