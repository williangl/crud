from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


def configure(app):
    db.init_app(app)
    app.db = db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    phone = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String, nullable=False)
    last_update = db.Column(
        db.DateTime,
        default=datetime.now,
        onupdate=datetime.now)
