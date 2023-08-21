from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.config["SECRET_KEY"] = "05646efc442447eb4b24b6a554d10d17"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from flaskblog import routes