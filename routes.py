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
	return render_template("band.html", info=bands.show_band_info(band_name))

@app.route("/register", methods=["get", "post"])
def register():
	if request.method == "GET":
		return render_template("register.html")

	if request.method == "POST":
		name = request.form["username"]
		# TÄHÄN VÄLIIN VAATIMUKSIA NIMIMERKISTÄ??
		password1 = request.form["password1"]
		password2 = request.form["password2"]

		#if password1 != password2:
			#return render_template(??)
			# TÄMÄ LOPPUUN
	role = request.form["role"]
	return redirect("/")

@app.route("/login", methods=["get", "post"])
def login():
	if request.method == "GET":
		return render_template("login.html")

	if request.method == "POST":
		name = request.form["username"]
		password = request.form["password"]

	#if not users.login(name, password):
		#return render_template(???) VIELÄ KESKEN

	return redirect("/")

