from app import app
from sqlalchemy.sql import text
from flask import redirect, render_template, request, session
from database import db
import bands
import users

@app.route("/")
def index():
	#result = db.session.execute(text("SELECT name FROM bands"))
	#bands = result.fetchall()
	return render_template("index.html", bands=bands.show_all_bands())

@app.route("/band_info/<string:band_name>")
def show_info(band_name):
	return render_template("band.html", info=bands.show_band_info(band_name))

@app.route("/reviews/<string:band_name>")
def show_reviews(band_name):
	try:
		return render_template("reviews.html", reviews=bands.show_reviews(band_name))
	except Exception as e:
	        return f"Error: {str(e)}"


@app.route("/register", methods=["get", "post"])
def register():
	if request.method == "GET":
		return render_template("register.html")

	if request.method == "POST":
		name = request.form["username"]
		if len(name) < 3 or len(name) > 15:
			return render_template("error.html", message="Käyttäjänimen tulee olla 3-15 merkkiä pitkä")
		password1 = request.form["password1"]
		password2 = request.form["password2"]

		if password1 != password2:
			return render_template("error.html", message="Salasanat ovat erit")
		if password1 == "":
			return render_template("error.html", message="Salasana ei voi olla tyhjä")

		role = request.form["role"]
		if not users.register(name, password1, role):
			return render_template("error.html", message="Rekisteröinti ei onnistunut :(")
		return redirect("/")

@app.route("/login", methods=["get", "post"])
def login():
	if request.method == "GET":
		return render_template("login.html")

	if request.method == "POST":
		name = request.form["name"]
		password = request.form["password"]

		if not users.login(name, password):
			return render_template("error.html", message="jotain meni väärin")

		return redirect("/")

@app.route("/logout")
def logout():
	users.logout()
	return redirect("/")

