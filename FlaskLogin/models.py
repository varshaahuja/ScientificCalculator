from flask_login import UserMixin
from . import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(64))

class History(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    num1 = db.Column(db.Float(100))
    num2 = db.Column(db.Float(100))
    op = db.Column(db.String(100))
    res = db.Column(db.Float(100))
    email=db.Column(db.String(100))
