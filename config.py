import os
from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy


# Loading environment variables
load_dotenv()

# Database variables
username = os.environ.get("db_username")
user_password = os.environ.get("password")
host = os.environ.get("host")
port = os.environ.get("port")
database = os.environ.get("database")

# URI for connecting to PostgreSQL
SQLALCHEMY_URI = f"postgresql://{username}:{user_password}@{host}:{port}/{database}"

# App Instantiate
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_URI

# Database Instantiate
db = SQLAlchemy()
db.init_app(app)