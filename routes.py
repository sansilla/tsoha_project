from app import app
from sqlalchemy.sql import text
from flask import redirect, render_template, request, session
from database import db
import bands

@app.route("/")
def index():
	#result = db.session.execute(text("SELECT name FROM bands"))
	#bands = result.fetchall()
	return render_template("index.html", bands=bands.show_all_bands())

@app.route("/band_info/<string:band_name>")
def show_info(band_name):
	#info = bands.show_band_info(band_id)
	return render_template("band.html", info=bands.show_band_info(band_name))

@app.route("/login", methods=["get", "post"])
def login():
	username = request.form["username"]
	password = request.form["password"]
