from flask import request
from app import app, db
from application.process.processModel import Process
from application.task.taskModel import Task
from application.logs.logsModel import Logs
from functions import send_success, send_warning

import threading
import subprocess
import psutil
import webbrowser
import time

class LauncherController:
    
    def launch_process(self, process,task):
                
        with app.app_context():
            
            details = process.name + " - " + task.name
                                    
            directory = task.directory
            command = task.command
            
            launchProcess = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, cwd=directory)
            
            pid = launchProcess.pid
                        
            logs = Logs(process_id = process.id, task_id = task.id, pid = pid, logs = details)
            db.session.add(logs)
            db.session.commit()
            
            launchProcess.wait()
            
    def launch_url(self, url, timeout):
        time.sleep(timeout)
        webbrowser.open(url)
            
    def killProcessByPID(self, parent_pid):
        try:
            parent = psutil.Process(parent_pid)
            for child in parent.children(recursive=True):
                child.kill()
            parent.kill()
        except:
            print('Error stopping process with pid %s' % (parent_pid,))
            
        with app.app_context():
            logs = Logs.query.filter(Logs.pid == parent_pid).first()
            db.session.delete(logs)
            db.session.commit()
    
    def launcher_process(self, id):
        
        process = Process.query.filter(Process.id == id).first()
        
        if process:
            
            tasks = Task.query.filter(Task.process_id == process.id)
            
            if tasks:
            
                for task in tasks:   
                                                                                     
                    threadProcess = threading.Thread(target=self.launch_process, args=[process,task])
                    threadProcess.start()
                    
                threadURL = threading.Thread(target=self.launch_url, args=[process.url,process.timeout])
                threadURL.start()
                                            
                response = send_success('El proceso fue ejecutado correctamente')
                return response
            
            else:
                response = send_warning('El proceso no tiene tareas asignadas')
                return response                
        else:
            response = send_warning('El proceso no existe')
            return response
        
        
    def stop_process_pid(self, pid):
        self.killProcessByPID(pid)
        response = send_success('El proceso con el PID asignado fue detenido correctamente')
        return response
    
    def stop_process_task_id(self, id):
        logs = Logs.query.filter(Logs.task_id == id)
        for task in logs:
            self.killProcessByPID(task.pid)
        response = send_success('La tarea fue detenida correctamente')
        return response
    
    def stop_process_id(self, id):
        logs = Logs.query.filter(Logs.process_id == id)
        for process in logs:
            self.killProcessByPID(process.pid)
        response = send_success('El proceso fue detenido correctamente')
        return response