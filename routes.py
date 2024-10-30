from flask import request, session
from app import app, session_name, session_name_tmp, session_theme
from flask import render_template, redirect

from application.utilities.auth import isAuth
    
@app.route('/changeTheme', methods=['GET'])
def theme():
    if request.method == 'GET':
        if not session.get(session_theme):
            session[session_theme] = 'dark'
        if session.get(session_theme) == 'dark':
            session[session_theme] = 'light'
        if session.get(session_theme) == 'light':
            session[session_theme] = 'dark'
        return {}
    
@app.route('/', methods=['GET'])
def ingreso():
    if isAuth() : return redirect('/dashboard')
    if request.method == 'GET':
        return render_template("ingreso/index.html")
    
@app.route('/dashboard/salir', methods=['GET'])
def salir():
    if not isAuth() : return redirect('/')
    if request.method == 'GET':
        session[session_name] = None
        session[session_name_tmp] = None
        session[session_theme] = None
        return redirect("/")
    
@app.route('/dashboard', methods=['GET'])
def dashboard():
    if not isAuth() : return redirect('/')
    if request.method == 'GET':
        return render_template("dashboard/index.html")
    
@app.route('/dashboard/procesos', methods=['GET'])
def listar_procesos():
    if not isAuth() : return redirect('/')
    if request.method == 'GET':
        return render_template("dashboard/procesos/index.html")
    
@app.route('/dashboard/procesos/nuevo', methods=['GET'])
def crear_proceso():
    if not isAuth() : return redirect('/')
    if request.method == 'GET':
        return render_template("dashboard/procesos/save.html")
    
@app.route('/dashboard/procesos/<int:process_id>/editar', methods=['GET'])
def editar_proceso(process_id):
    if not isAuth() : return redirect('/')
    if request.method == 'GET':
        return render_template("dashboard/procesos/save.html", process_id = process_id)
 
@app.route('/dashboard/procesos/<int:process_id>/borrar', methods=['GET'])
def borrar_proceso(process_id):
    if not isAuth() : return redirect('/')
    if request.method == 'GET':
        return render_template("dashboard/procesos/delete.html", process_id = process_id)
    
@app.route('/dashboard/procesos/<int:process_id>/tareas', methods=['GET'])
def tareas_proceso(process_id):
    if not isAuth() : return redirect('/')
    if request.method == 'GET':
        return render_template("dashboard/tareas/index.html", process_id = process_id)
    
@app.route('/dashboard/procesos/<int:process_id>/tareas/nuevo', methods=['GET'])
def crear_tarea(process_id):
    if not isAuth() : return redirect('/')
    if request.method == 'GET':
        return render_template("dashboard/tareas/save.html", process_id = process_id)
    
@app.route('/dashboard/procesos/<int:process_id>/tareas/<int:task_id>/editar', methods=['GET'])
def editar_tarea(process_id,task_id):
    if not isAuth() : return redirect('/')
    if request.method == 'GET':
        return render_template("dashboard/tareas/save.html", process_id = process_id, task_id = task_id)
    
@app.route('/dashboard/procesos/<int:process_id>/tareas/<int:task_id>/borrar', methods=['GET'])
def borrar_tarea(process_id,task_id):
    if not isAuth() : return redirect('/')
    if request.method == 'GET':
        return render_template("dashboard/tareas/delete.html", process_id = process_id , task_id = task_id)
    
@app.route('/dashboard/logs', methods=['GET'])
def logs():
    if not isAuth() : return redirect('/')
    if request.method == 'GET':
        return render_template("dashboard/logs/index.html")
    
@app.route('/dashboard/logs/<int:logs_id>/cerrarTarea', methods=['GET'])
def logs_cerrar_tarea(logs_id):
    if not isAuth() : return redirect('/')
    if request.method == 'GET':
        return render_template("dashboard/logs/close-task.html", logs_id = logs_id)
    
@app.route('/dashboard/logs/<int:logs_id>/cerrarProceso', methods=['GET'])
def logs_cerrar_proceso(logs_id):
    if not isAuth() : return redirect('/')
    if request.method == 'GET':
        return render_template("dashboard/logs/close-process.html", logs_id = logs_id)    

@app.route('/dashboard/cuenta', methods=['GET'])
def cuenta():
    if not isAuth() : return redirect('/')
    if request.method == 'GET':
        return render_template("dashboard/cuenta/index.html")