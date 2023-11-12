from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Pic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(100))
    data = db.Column(db.LargeBinary)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True) # unique = True กันคนซ้ำ
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    pic = db.relationship('Pic')
    


