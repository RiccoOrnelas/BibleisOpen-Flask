from db import db
from flask import request, Blueprint, current_app
from models.models import User
from models.models import Devotional

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/createUser", methods=["POST"])
def createUser():
    name = request.form.get("name")
    email = request.form.get("email")
    senha = request.form.get("password")
    user = User(username=name, email=email, password=senha)
    db.session.add(user)
    db.session.commit()
    return f"{name} adiconado com sucesso"


@auth_bp.route("/createDevotional", methods=["POST"])
def createDevotional():
    title = request.form.get("title")
    content = request.form.get("content")
    file = request.form.get("file")
    devotional = User(username=name, email=email, password=senha)
    db.session.add(user)
    db.session.commit()
    return f"{name} adiconado com sucesso"
