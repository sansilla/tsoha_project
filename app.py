from flask import Flask
from os import getenv

app = Flask(__name__)
#app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///sansilla" EI VARMAAN TARVITA ENÄÄ?

import routes
