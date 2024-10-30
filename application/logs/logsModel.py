from app import db
from marshmallow import fields, Schema
from datetime import datetime

class Logs(db.Model):
    __tablename__ = 'logs'
    id = db.Column(db.Integer(), primary_key=True)
    process_id = db.Column(db.Integer(), db.ForeignKey('processes.id'))
    task_id = db.Column(db.Integer(), db.ForeignKey('tasks.id'))
    pid = db.Column(db.Integer())
    logs = db.Column(db.Text())
    created_at = db.Column(db.DateTime(timezone = True), default = datetime.now)
    updated_at = db.Column(db.DateTime(timezone = True), default = datetime.now, onupdate = datetime.now)
    
class LogsSchema(Schema):
    id = fields.Int(data_key='id')
    process_id = fields.Int(data_key='process_id')
    task_id = fields.Int(data_key='task_id')
    pid = fields.Int(data_key='pid')
    logs = fields.Str(data_key='logs')
    created_at = fields.Str(data_key='created_at')
    updated_at = fields.Str(data_key='updated_at')