from database import db
from sqlalchemy.sql import text

def show_all_bands():
	sql = "SELECT name FROM bands ORDER BY name"
	return db.session.execute(text(sql)).fetchall()

def show_band_info(band_name):
	sql = "SELECT band_name, info_text FROM info WHERE band_name=band_name"
	return db.session.execute(text(sql)).fetchone()
