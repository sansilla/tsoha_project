from database import db
from sqlalchemy.sql import text

def show_all_bands():
	sql = "SELECT name FROM bands ORDER BY name"
	return db.session.execute(text(sql)).fetchall()

def show_band_info(band_name):
	sql = "SELECT band_name, info_text FROM info WHERE band_name=:band_name"
	return db.session.execute(text(sql), {"band_name": band_name}).fetchone()

def show_reviews(band_name):
	sql = "SELECT bands.name, reviews.comment FROM bands JOIN reviews ON bands.id=reviews.band_id WHERE bands.name=:band_name"
	#sql = "SELECT bands.name, reviews.comment FROM bands, reviews WHERE bands.id=reviews.band_id AND bands.name=:band_name"
	return db.session.execute(text(sql), {"band_name": band_name}).fetchall()

def add_review(band_id, user_id, comment):
	sql = "INSERT INTO reviews (band_id, user_id, comment) VALUES (:band_id, :user_id, :comment)"
	db.session.execute(text(sql), {"comment":comment, "user_id":user_id, "band_id":band_id})
	db.session.commit()
	return True
	#VIELÄ KESKEN
