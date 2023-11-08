#Vasta testailua!
from flask import Flask
from flask import redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///sansilla"
db = SQLAlchemy(app)

@app.route("/")
def index():
	result = db.session.execute(text("SELECT name FROM bands"))
	bands = result.fetchall()
	return render_template("index.html", bands=bands)
	#return "Hallooo :("
