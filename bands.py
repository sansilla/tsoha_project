from database import db
from sqlalchemy.sql import text

def show_all_bands():
	sql = "SELECT name FROM bands ORDER BY name"
	return db.session.execute(text(sql)).fetchall()

def show_band_info(band_name):
	sql = "SELECT bands.name, info.info_text FROM bands, info WHERE bands.name=info.band_name"
	return db.session.execute(text(sql)).fetchone()
