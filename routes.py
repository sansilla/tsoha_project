from app import app
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

@app.route("/delete_from_favourites", methods=["POST"])
def delete_from_favourites():
	user_id = session["user_id"]
	band_name = request.form.get("band_name")
	band_id = bands.get_band_id(band_name)

	bands.delete_from_favourites(user_id, band_id)

	return redirect(request.referrer)

@app.route("/favourites")
def show_favourites():
	user_id = session["user_id"]
	return render_template("favourites.html", favourites=bands.show_favourites(user_id))

@app.route("/reviews/<string:band_name>")
def show_reviews(band_name):
	try:
		return render_template("reviews.html", reviews=bands.show_reviews(band_name), band_name=band_name)

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

		band_id = bands.get_band_id(band_name)
		comment = request.form["comment"]
		if comment == "":
			return render_template("error.html", message="arvostelu ei voi olla tyhjä", link=request.referrer, text="Takaisin arvosteluihin")

		if len(comment) > 200:
			return render_template("error.html", message="arvostelu voi olla max. 200 merkkiä", link=request.referrer, text="Takaisin arvosteluihin")

		bands.add_review(band_id, users.user_id(), comment)

		return redirect(f"/reviews/{band_name}")

	except Exception as e:
		return f"Error: {str(e)} :("

@app.route("/remove_review", methods=["POST"])
def remove_review_route():
	users.must_have_role(2)
	comment = request.form.get("comment")
	user_name = request.form.get("user_name")

	bands.remove_review(comment, user_name)

	return redirect(request.referrer)

@app.route("/add_band", methods=["get", "post"])
def add_band():
	if request.method == "GET":
		return render_template("add_band.html")

	if request.method == "POST":
		users.must_have_role(2)
		users.check_csrf()

		band_name = request.form["band_name"]
		if band_name == "":
			return render_template("error.html", message="nimi ei voi olla tyhjä", link="/add_band", text="Takaisin bändin lisäämiseen")
		info_text = request.form["info_text"]
		if info_text == "":
			return render_template("error.html", message="kirjoita bändille kuvaus", link="/add_band", text="Takaisin bändin lisäämiseen")

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
			return render_template("error.html", message="käyttäjänimen tulee olla 3-15 merkkiä pitkä", link="/register", text="Takaisin rekisteröintiin")

		password1 = request.form["password1"]
		password2 = request.form["password2"]

		if password1 != password2:
			return render_template("error.html", message="salasanat ovat erit", link="/register", text="Takaisin rekisteröintiin")
		if password1 == "":
			return render_template("error.html", message="salasana ei voi olla tyhjä", link="/register", text="Takaisin rekisteröintiin")
		if len(password1) < 5 or len(password1) > 20:
			return render_template("error.html", message="salananan tulee olla 5-20 merkkiä pitkä", link="/register", text="Takaisin rekisteröintiin")

		role = request.form["role"]
		reg_result = users.register(name, password1, role)

		if reg_result == "username_exists":
			return render_template("error.html", message="käyttäjänimi on jo käytössä", link="/register", text="Takaisin rekisteröintiin")

		return redirect("/")

@app.route("/login", methods=["get", "post"])
def login():
	if request.method == "GET":
		return render_template("login.html")

	if request.method == "POST":
		name = request.form["name"]
		password = request.form["password"]

		if name == "":
			return render_template("error.html", message="kirjoita käyttäjänimi", link="/login", text="Takaisin sisäänkirjautumiseen")
		
		if password == "":
			return render_template("error.html", message="kirjoita salasana", link="/login", text="Takaisin sisäänkirjautumiseen")

		login_result = users.login(name, password)
		if login_result == "not_exists":
			return render_template("error.html", message="käyttäjänimeä ei ole olemassa", link="/login", text="Takaisin sisäänkirjautumiseen")
		
		if login_result == "wrong_password":
			return render_template("error.html", message="väärä salasana", link="/login", text="Takaisin sisäänkirjautumiseen")

		return redirect("/")

@app.route("/logout")
def logout():
	users.logout()
	return redirect("/")

