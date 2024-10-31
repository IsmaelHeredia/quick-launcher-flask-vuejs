# Quick Launcher

En este proyecto se hizo un sistema para lanzar procesos en segundo plano que usa Flask con Bootstrap 5, usando MySQL para gestionar los datos de la aplicación. Esta pensando para gestionar servidores y facilitar los manejos de los comandos de cada uno, ya sean de proyectos de Laravel, NodeJS, Angular, React o cualquier otro. También incluye una función para que ejecute en el navegador la URL del proceso ejecutado después de un tiempo de espera asignado en el sistema.

Las funciones incorporadas son : 

Inicio de sesión obligatorio para usar el sistema protegido con JWT.

Posibilidad de cambiar usuario y contraseña.

Posibilidad de cambiar el theme completo del sistema a un modo oscuro o claro.

Se puede agregar, editar y borrar procesos. En la sección de procesos se pueden gestionar las tareas de cada proceso.

En la página principal se listan todas los procesos registrados donde se pueden ejecutar y detener las tareas de cada uno. También hay una sección de logs donde se muestran los procesos activos con sus PID asociados y se pueden cerrar por tarea o por proceso.

A continuación se muestran unas imágenes del sistema en funcionamiento.

![screenshot]()

Para la correcta instalación del sistema se deben seguir los siguiente pasos. 

En la carpeta principal se debe renombrar el archivo .env.example a solo .env y editar la configuración con los datos de tu conexión MySQL, el SECRET_KEY que seria la clave para generar el JWT.

Para instalar la librería de conexión a MySQL en Linux el comando debería ser :

```
sudo apt-get install python3-pymysql
```

De lo contrario si están usando Windows seria :

```
pip install PyMySQL
```

Posteriormente debemos terminar de instalar las dependencias con el siguiente comando : 

```
pip install -r requirements.txt
```

Para ejecutar Flask en Windows se debe hacer de la siguiente manera : 

```
python -m flask
```

De lo contrario si están usando Linux bastaría con usar simplemente el comando flask, teniendo en cuenta esto para ejecutar las migraciones de Flask deben ejecutar los siguientes comandos :

```
flask db init
```
```
flask db migrate
```
```
flask db upgrade
```
```
flask seed
```

Finalmente para iniciar el sistema se debe ejecutar este comando : 

```
flask --app main.py --debug run --port=8888
```