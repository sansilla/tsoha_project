from app import app
from sqlalchemy.sql import text
from flask import redirect, render_template, request, session
from database import db
import bands
import users

@app.route("/")
def index():
	return render_template("index.html", bands=bands.show_all_bands())

@app.route("/band_info/<string:band_name>")
def show_info(band_name):
	return render_template("band.html", info=bands.show_band_info(band_name))

@app.route("/add_to_favourites", methods=["POST"])
def add_to_favourites():
	user_id = session["user_id"]
	band_name = request.form.get("band_name")
	band_id = bands.get_band_id(band_name)

	bands.add_to_favourites(user_id, band_id)

	return redirect(request.referrer)

@app.route("/favourites")
def show_favourites():
	user_id = session["user_id"]
	#user_id = users.user_id()
	return render_template("favourites.html", favourites=bands.show_favourites(user_id))

@app.route("/reviews/<string:band_name>")
def show_reviews(band_name):
	try:
		#band_id = bands.get_band_id(band_name)
		#if band_id is not None:
		return render_template("reviews.html", reviews=bands.show_reviews(band_name), band_name=band_name)
		#else:
			#return "Band not found"
	except Exception as e:
	        return f"Error: {str(e)}"

@app.route("/reviews/<string:band_name>", methods=["post"])
def give_review(band_name):
	try:
		if 'csrf_token' not in session or 'csrf_token' not in request.form:
			return "CSRF Token missing"
		if session["csrf_token"] != request.form["csrf_token"]:
        		return "CSRF Error"
		users.must_have_role(1)
		users.check_csrf()

		#band_name = request.form["band_name"]
		band_id = bands.get_band_id(band_name)
		comment = request.form["comment"]

		bands.add_review(band_id, users.user_id(), comment)
		print("toimiiko")
	#return True
		return redirect(f"/reviews/{band_name}") #("/reviews/<string:band_name")
		#return redirect(url_for("show_reviews", band_name=band_name))
	except Exception as e:
		return f"Error: {str(e)} :("

#@app.route("/remove", methods=["get", "post"])
#def remove_review():
	#users.must_have_role(2)
	#if request.method == "GET":
		#r_views = bands.show_reviews(???)

@app.route("/add_band", methods=["get", "post"])
def add_band():
	if request.method == "GET":
		return render_template("add_band.html")

	if request.method == "POST":
		users.must_have_role(2)
		users.check_csrf()

		band_name = request.form["band_name"]
		info_text = request.form["info_text"]

		bands.add_band(band_name) 
		bands.add_info(band_name, info_text)

		return redirect("/")

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

