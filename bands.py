from database import db
from sqlalchemy.sql import text

def show_all_bands():
	sql = "SELECT name FROM bands"
	return db.session.execute(text(sql)).fetchall()
