import os
from flask import request, session
from database import db
from werkzeug.security import check_password_hash, generate_password_hash

def register(name, password, role):
	hash_value = generate_password_hash(password)
	sql = "INSERT INTO users (name, password, role) VALUES (:name

def login(name, password):
	sql = "SELECT id, password, role FROM users WHERE name=:name"
	returning = db.session.execute(sql, {"name":name})
	#JATKA TÄTÄ MYÖHEMMIN

