import os
from flask import request, session, abort
from database import db
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy import text

def register(name, password, role):
	hash_value = generate_password_hash(password)
	try:
		sql = text("INSERT INTO users (name, password, role) VALUES (:name, :password, :role)")
		print(sql)
		db.session.execute(sql, {"name":name, "password":hash_value, "role":role})
		print("apua")
		db.session.commit()
		#return True

	#except:
		#return False

	except Exception as e:
        	print(f"Error inserting into database: {e}")
        	return False

	return login(name, password)


def login(name, password):
	sql = text("SELECT password, id, role FROM users WHERE name=:name")
	returning = db.session.execute(sql, {"name":name})
	user = returning.fetchone()
	if not user:
		return False
	if not check_password_hash(user[0], password):
		return False
	session["user_id"] = user[1]
	session["user_name"] = name
	session["user_role"] = user[2]
	session["csfr_token"] = os.urandom(16).hex()
	return True

def user_id():
	return session.get("user_id", 0)

def check_csrf():
	if session["csrf_token"] != request.form["csrf_token"]:
		abort(403)

def logout():
	del session["user_id"]
	del session["user_name"]
	del session["user_role"]

def must_have_role(role):
	if role > session.get("user_role", 0):
		abort(403)
