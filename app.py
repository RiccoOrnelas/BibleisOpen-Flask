from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__, template_folder="views")

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

from db import db

db.init_app(app)

migrate = Migrate(app, db)

from models.models import User, Devotional, Comments


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/newDevotional")
def newDevotional():
    return render_template("newDevotional.html")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
