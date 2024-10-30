from flask import request
from app import app

from application.utilities.auth import AuthBack

from application.user.userController import UserController
from application.process.processController import ProcessController
from application.task.taskController import TaskController
from application.logs.logsController import LogsController
from application.launcher.launcherController import LauncherController

@app.route('/api/login', methods=['POST'])
def login():
    controller = UserController()
    if request.method == 'POST':
        return controller.login()
    
@app.route('/api/validate', methods=['POST'])
def validate():
    controller = UserController()
    if request.method == 'POST':
        return controller.validate()
        
@app.route('/api/processes', methods=['GET', 'POST'])
@AuthBack()
def processesApi():
    controller = ProcessController()
    if request.method == 'POST':
        return controller.create()
        
    if request.method == 'GET':
        return controller.getAll()
    
@app.route('/api/processes/<int:id>', methods=['GET', 'PUT', 'DELETE'])
@AuthBack()
def processesApiDetails(id):
    controller = ProcessController()
    if request.method == 'GET':
        return controller.get(id)
    
    if request.method == 'PUT':
        return controller.update(id)
    
    if request.method == 'DELETE':
        return controller.delete(id)
    
    
@app.route('/api/processes/<int:id>/tasks', methods=['GET'])
@AuthBack()
def processesTasksApiDetails(id):
    controller = ProcessController()
    if request.method == 'GET':
        return controller.getTasks(id)
     
@app.route('/api/tasks', methods=['GET', 'POST'])
@AuthBack()
def tasksApi():
    controller = TaskController()
    if request.method == 'POST':
        return controller.create()
        
    if request.method == 'GET':
        return controller.getAll()
    
@app.route('/api/tasks/<int:id>', methods=['GET', 'PUT', 'DELETE'])
@AuthBack()
def tasksApiDetails(id):
    controller = TaskController()
    if request.method == 'GET':
        return controller.get(id)
    
    if request.method == 'PUT':
        return controller.update(id)
    
    if request.method == 'DELETE':
        return controller.delete(id) 
        
@app.route('/api/account', methods=['POST'])
@AuthBack()
def accountApi():
    controller = UserController()
    if request.method == 'POST':
        return controller.account()
        
@app.route('/api/launcher/process/<int:id>/start', methods=['GET'])
@AuthBack()
def launcherStartApi(id):
    controller = LauncherController()
    if request.method == 'GET':
        return controller.launcher_process(id)
                
@app.route('/api/launcher/pid/<int:pid>/stop', methods=['GET'])
@AuthBack()
def launcherStopPidApi(pid):
    controller = LauncherController()
    if request.method == 'GET':
        return controller.stop_process_pid(pid)
    
@app.route('/api/launcher/task/<int:id>/stop', methods=['GET'])
@AuthBack()
def launcherStopTaskApi(id):
    controller = LauncherController()
    if request.method == 'GET':
        return controller.stop_process_task_id(id)
    
@app.route('/api/launcher/process/<int:id>/stop', methods=['GET'])
@AuthBack()
def launcherStopProcessApi(id):
    controller = LauncherController()
    if request.method == 'GET':
        return controller.stop_process_id(id)
    
@app.route('/api/logs', methods=['GET'])
@AuthBack()
def logsApi():
    controller = LogsController()

    if request.method == 'GET':
        return controller.getAll()
    
@app.route('/api/logs/<int:id>', methods=['GET'])
@AuthBack()
def logsApiDetails(id):
    controller = LogsController()
    if request.method == 'GET':
        return controller.get(id)