from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from controllers.auth import createUser, auth_bp, createDevotional
from models.models import User, Devotional, Comments


app = Flask(__name__, template_folder="views")

app.jinja_env.globals["createUser"] = createUser
app.jinja_env.globals["createDevotional"] = createDevotional


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


app.route("/createUser", methods=["POST"])(createUser)
app.route("/createDevotional", methods=["POST"])(createDevotional)


app.register_blueprint(auth_bp)

from db import db

db.init_app(app)
migrate = Migrate(app, db)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/newDevotional")
def newDevotional():
    return render_template("newDevotional.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/login")
def login():
    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)


# Criar Post Para Registro de Usuário

# Autenticação de Usuário

# Mensageria de Usuário

# Arrumar um meio de capturar o usuário e identificar no Devotional

# Criar Post Para Registro de Devocional

# Criar Post Para Registro de Devocional
