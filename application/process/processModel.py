from app import db
from marshmallow import fields, Schema
from datetime import datetime

class Process(db.Model):
    __tablename__ = 'processes'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(150),unique=True)
    url = db.Column(db.Text())
    timeout = db.Column(db.Integer())
    created_at = db.Column(db.DateTime(timezone = True), default = datetime.now)
    updated_at = db.Column(db.DateTime(timezone = True), default = datetime.now, onupdate = datetime.now)
    
    task = db.relationship('Task', backref = 'task')
    
class ProcessSchema(Schema):
    id = fields.Int(data_key='id')
    name = fields.Str(data_key='name')
    url = fields.Str(data_key='url')
    timeout = fields.Int(data_key='timeout')
    created_at = fields.Str(data_key='created_at')
    updated_at = fields.Str(data_key='updated_at')