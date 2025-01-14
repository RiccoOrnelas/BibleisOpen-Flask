from datetime import datetime
from db import db  # Importando a instância db de models/__init__.py


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    devotionals = db.relationship("Devotional", backref="author", lazy=True)


class Devotional(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(200), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship("User", backref="devotionals", lazy=True)


class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    devotional_id = db.Column(
        db.Integer, db.ForeignKey("devotional.id"), nullable=False
    )
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
