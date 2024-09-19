import os
from flask import Flask
from dotenv import load_dotenv
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


# Loading environment variables
load_dotenv()

# Getting database variables from environment
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
migrate = Migrate(app, db)
db.init_app(app)
