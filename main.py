from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import SQLALCHEMY_URI
import models

# connecting
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_URI
db = SQLAlchemy()
db.init_app(app)

# routes
@app.route("/")
def index():

	return "Hello, it's work!"


if __name__ == "__main__":
	app.run(debug=True)
