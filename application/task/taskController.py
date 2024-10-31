from flask import request
from app import db
from application.task.taskModel import Task, TaskSchema
from schemas import ValidateTaskSchema
from functions import send_success, send_warning
from marshmallow import ValidationError

class TaskController:
    
    def getAll(self):
        tasks = Task.query.order_by(Task.updated_at.desc()).all()
        data = TaskSchema(many=True).dump(tasks)
        response = send_success('Las tareas se listaron correctamente', data)
        return response
    
    def create(self):
        request_data = request.json
        schema = ValidateTaskSchema()
        try:
            result = schema.load(request_data)
            name = result['name']
            directory = result['directory']
            command = result['command']
            process_id = result['process_id']
            try:
                task = Task(name = name, directory = directory, command = command, process_id = process_id)
                db.session.add(task)
                db.session.commit()
                response = send_success('La tarea fue registrada correctamente', task.id)
                return response
            except:
                response = send_warning('Ocurrío un error en creando la tarea')
                return response
            
        except ValidationError as err:
            response = send_warning(err.messages)
            return response
        
    def get(self, id):
        task = Task.query.filter(Task.id == id).first()
        if task:
            data = TaskSchema().dump(task)
            response = send_success('La tarea se cargo correctamente', data)
            return response
        else:
            response = send_warning('La tarea no existe')
            return response
        
    def update(self, id):
        request_data = request.json
        schema = ValidateTaskSchema()
        try:
            result = schema.load(request_data)
            name = result['name']
            directory = result['directory']
            command = result['command']
            process_id = result['process_id']
            task = Task.query.filter(Task.id == id).first()
            if task:
                task.name = name
                task.directory = directory
                task.command = command
                task.process_id = process_id
                try:
                    db.session.commit()
                    response = send_success('La tarea se actualizó correctamente', task.id)
                    return response
                except:
                    response = send_warning('Ocurrío un error actualizado la tarea')
                    return response
            else:
                response = send_warning('La tarea no existe')
                return response
        except ValidationError as err:
            response = send_warning(err.messages)
            return response
        
    def delete(self, id):
        task = Task.query.filter(Task.id == id).first()
        if task:
            try:
                db.session.delete(task)
                db.session.commit()
                response = send_success('La tarea se borró correctamente')
                return response
            except:
                response = send_warning('Ocurrío un error borrando la tarea')
                return response
        else:
            response = send_warning('La tarea no existe')
            return response  