from database import db
from sqlalchemy.sql import text

def show_all_bands():
	sql = "SELECT name FROM bands ORDER BY name"
	return db.session.execute(text(sql)).fetchall()

def get_band_id(band_name):
	sql = db.session.execute(text("SELECT id FROM bands WHERE name=:name"), {"name": band_name})
	band = sql.fetchone()
	return band[0] if band else None

def show_band_info(band_name):
	sql = "SELECT band_name, info_text FROM info WHERE band_name=:band_name"
	return db.session.execute(text(sql), {"band_name": band_name}).fetchone()

def add_to_favourites(user_id, band_id):
	already_in_list = db.session.execute(text("SELECT id FROM favourites WHERE user_id=:user_id AND band_id=:band_id"), {"user_id": user_id, "band_id":band_id}).fetchone()
	if already_in_list:
		pass
	else:
		print(f"Adding to favourites: user_id={user_id}, band_id={band_id}")
		sql = "INSERT INTO favourites (user_id, band_id) VALUES (:user_id, :band_id)"
		db.session.execute(text(sql), {"user_id":user_id, "band_id":band_id})
		db.session.commit()

def delete_from_favourites(user_id, band_id):
	print(f"Deleting from favourites: user_id={user_id}, band_id={band_id}")
	sql = "DELETE FROM favourites WHERE user_id=:user_id AND band_id=:band_id"
	db.session.execute(text(sql), {"user_id":user_id, "band_id":band_id})
	db.session.commit()

def show_favourites(user_id):
	sql = "SELECT bands.name FROM bands JOIN favourites ON bands.id=favourites.band_id WHERE favourites.user_id=:user_id"
	return db.session.execute(text(sql), {"user_id": user_id}).fetchall()

def show_reviews(band_name):
	#sql = "SELECT bands.name, reviews.user_id, reviews.comment FROM bands JOIN reviews ON bands.id=reviews.band_id WHERE bands.name=:band_name"

	sql = "SELECT users.name AS user_name, reviews.comment, bands.name FROM bands JOIN reviews ON bands.id=reviews.band_id JOIN users ON reviews.user_id=users.id WHERE bands.name=:band_name"
	#tämän täytyisi saada näyttämään jotain (edes vaikka 0) jos bändistä ei vielä ole arvosteluja

	return db.session.execute(text(sql), {"band_name": band_name}).fetchall()

def add_review(band_id, user_id, comment):
	#sql = "INSERT INTO reviews (band_id, user_id, comment) VALUES ((SELECT id FROM bands WHERE name=:band_name), :user_id, :comment"
	sql = "INSERT INTO reviews (band_id, user_id, comment) VALUES (:band_id, :user_id, :comment)"
	db.session.execute(text(sql), {"band_id":band_id, "user_id":user_id, "comment":comment})
	db.session.commit()
	return True

def remove_review(comment, user_name):
	print(f"Deleting from reviews: comment={comment}, user_name={user_name}")
	sql = "DELETE FROM reviews WHERE comment=:comment AND user_id=(SELECT id from users WHERE name=:user_name)"
	#sql = "DELETE FROM reviews WHERE comment=:comment AND user_id=:user_id"
	db.session.execute(text(sql), {"comment":comment, "user_name":user_name})
	db.session.commit()
	#tämä on vasta luonnostelua

def add_band(band_name):
	sql = "INSERT INTO bands (name) VALUES (:band_name)"
	db.session.execute(text(sql), {"band_name": band_name})
	db.session.commit()

def add_info(band_name, info_text):
	sql = "INSERT INTO info (band_name, info_text) VALUES (:band_name, :info_text)"
	db.session.execute(text(sql), {"band_name": band_name, "info_text": info_text})
	db.session.commit()
