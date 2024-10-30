from app import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(150),unique=True)
    pwd = db.Column(db.Text())
    created_at = db.Column(db.DateTime(timezone=True), default = datetime.now)
    updated_at = db.Column(db.DateTime(timezone=True), default = datetime.now, onupdate = datetime.now)