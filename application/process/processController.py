from flask import request
from app import db
from application.task.taskModel import Task, TaskSchema
from application.process.processModel import Process, ProcessSchema
from schemas import ValidateProcessSchema
from functions import send_success, send_warning
from marshmallow import ValidationError

class ProcessController:
    
    def getAll(self):
        processes = Process.query.all()
        data = ProcessSchema(many=True).dump(processes)
        response = send_success('Los procesos se listaron correctamente', data)
        return response
    
    def create(self):
        request_data = request.json
        schema = ValidateProcessSchema()
        try:
            result = schema.load(request_data)
            name = result['name']
            url = result['url']
            timeout = result['timeout']
            try:
                process = Process(name = name, url = url, timeout = timeout)
                db.session.add(process)
                db.session.commit()
                response = send_success('El proceso fue registrado correctamente', process.id)
                return response
            except:
                response = send_warning('Ocurrío un error en creando el proceso')
                return response
            
        except ValidationError as err:
            response = send_warning(err.messages)
            return response
        
    def get(self, id):
        process = Process.query.filter(Process.id == id).first()
        if process:
            data = ProcessSchema().dump(process)
            response = send_success('El proceso se cargo correctamente', data)
            return response
        else:
            response = send_warning('El proceso no existe')
            return response
        
    def getTasks(self, id):
        process = Process.query.filter(Process.id == id).first()
        tasks = Task.query.filter(Task.process_id == id).all()
        if process and tasks:
            data_process = ProcessSchema().dump(process)
            data_tasks = TaskSchema(many=True).dump(tasks)
            data = {}
            data['process'] = data_process
            data['tasks'] = data_tasks
            response = send_success('Las tareas del proceso se cargaron correctamente', data)
            return response
        else:
            response = send_warning('El proceso no existe')
            return response
        
    def update(self, id):
        request_data = request.json
        schema = ValidateProcessSchema()
        try:
            result = schema.load(request_data)
            name = result['name']
            url = result['url']
            timeout = result['timeout']
            process = Process.query.filter(Process.id == id).first()
            if process:
                process.name = name
                process.url = url
                process.timeout = timeout
                try:
                    db.session.commit()
                    response = send_success('El proceso se actualizó correctamente', process.id)
                    return response
                except:
                    response = send_warning('Ocurrío un error actualizado el proceso')
                    return response
            else:
                response = send_warning('El proceso no existe')
                return response
        except ValidationError as err:
            response = send_warning(err.messages)
            return response
        
    def delete(self, id):
        process = Process.query.filter(Process.id == id).first()
        if process:
            try:
                db.session.delete(process)
                db.session.commit()
                response = send_success('El proceso se borró correctamente')
                return response
            except:
                response = send_warning('Ocurrío un error borrando el proceso')
                return response
        else:
            response = send_warning('El proceso no existe')
            return response