from app import app
from sqlalchemy.sql import text
from flask import redirect, render_template, request
from database import db
import bands

@app.route("/")
def index():
	#result = db.session.execute(text("SELECT name FROM bands"))
	#bands = result.fetchall()
	return render_template("index.html", bands=bands.show_all_bands())
