from flask import request
from app import db
from application.logs.logsModel import Logs, LogsSchema
from functions import send_success, send_warning

class LogsController:
    
    def getAll(self):
        logs = Logs.query.order_by(Logs.updated_at.desc()).all()
        data = LogsSchema(many=True).dump(logs)
        response = send_success('Los registros de logs se listaron correctamente', data)
        return response

    def get(self, id):
        logs = Logs.query.filter(Logs.id == id).first()
        if logs:
            data = LogsSchema().dump(logs)
            response = send_success('El registro se cargo correctamente', data)
            return response
        else:
            response = send_warning('El registro no existe')
            return response