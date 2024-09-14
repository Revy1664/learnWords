import os
from dotenv import load_dotenv


# loading environment variables
load_dotenv()

# database variables
username = os.environ.get("db_username")
user_password = os.environ.get("password")
host = os.environ.get("host")
port = os.environ.get("port")
database = os.environ.get("database")

SQLALCHEMY_URI = f"postgresql://{username}:{user_password}@{host}:{port}/{database}"
