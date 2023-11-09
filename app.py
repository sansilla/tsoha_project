from flask import Flask
from flask import redirect, render_template, request
#from flask_sqlalchemy import SQLAlchemy SIIRRETTY DATABASEEN
from sqlalchemy.sql import text
#from os import getenv SIIRRETTY DATABASEEN

app = Flask(__name__)
#app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL") SIIRRETTY DATABASEEN
#app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///sansilla" EI VARMAAN TARVITA ENÄÄ?
#db = SQLAlchemy(app) SIIRRETTY DATABASEEN

@app.route("/")
def index():
	result = db.session.execute(text("SELECT name FROM bands"))
	bands = result.fetchall()
	return render_template("index.html", bands=bands)
	#return "Hallooo :("
