from app import db
from marshmallow import fields, Schema
from datetime import datetime

class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(150))
    directory = db.Column(db.Text())
    command = db.Column(db.Text())
    process_id = db.Column(db.Integer(), db.ForeignKey('processes.id'))
    created_at = db.Column(db.DateTime(timezone = True), default = datetime.now)
    updated_at = db.Column(db.DateTime(timezone = True), default = datetime.now, onupdate = datetime.now)
    
class TaskSchema(Schema):
    id = fields.Int(data_key='id')
    name = fields.Str(data_key='name')
    directory = fields.Str(data_key='directory')
    command = fields.Str(data_key='command')
    created_at = fields.Str(data_key='created_at')
    updated_at = fields.Str(data_key='updated_at')
    process = fields.Nested('ProcessSchema', only = ('id', 'name', 'url', 'timeout'))