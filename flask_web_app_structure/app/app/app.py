from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os
from .constantes import SECRET_KEY

chemin_actuel = os.path.dirname(os.path.abspath(__file__))

templates = os.path.join(chemin_actuel, "templates")

statics = os.path.join(chemin_actuel, "static")

app = Flask(
    "Application",
    template_folder=templates,
    static_folder=statics
)

db = SQLAlchemy()

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./bdd.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.config['SECRET_KEY'] = SECRET_KEY

login = LoginManager()

#On met en place le gestionnaire d'utilisateurs.

from .routes import generic
from .routes import api


