# Quick Launcher

En este proyecto se hizo un sistema para lanzar procesos en segundo plano que usa Flask con Bootstrap 5, usando MySQL para gestionar los datos de la aplicación. Esta pensando para gestionar servidores y facilitar los manejos de los comandos de cada uno, ya sean de proyectos de Laravel, NodeJS, Angular, React o cualquier otro. También incluye una función para que ejecute en el navegador la URL del proceso ejecutado después de un tiempo de espera asignado en el sistema.

Las funciones incorporadas son : 

Inicio de sesión obligatorio para usar el sistema protegido con JWT.

Posibilidad de cambiar usuario y contraseña.

Posibilidad de cambiar el theme completo del sistema a un modo oscuro o claro.

Se puede agregar, editar y borrar procesos. En la sección de procesos se pueden gestionar las tareas de cada proceso.

En la página principal se listan todas los procesos registrados donde se pueden ejecutar y detener las tareas de cada uno. También hay una sección de logs donde se muestran los procesos activos con sus PID asociados y se pueden cerrar por tarea o por proceso.

A continuación se muestran unas imágenes del sistema en funcionamiento.

![screenshot](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjl6ATiQYsv4tf5wrrBRys-Wlyj5ljQuofE2lRkQEZKuJmPL_ASnUmkKfkR_5-jyvC1stzVWPiNKc4HTZGXyXxawiPcss5CqH4Th-BhAAI4laXHApVPZdHpt76ADjI_KVi9P0WnSLOD5LkX-1cHbYyatvXTQzb1L5j9uGL-tH0AvbhmVvEvSU7CxOYJ1EQ/s1843/1.png)

![screenshot](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjyg6omlm3iwcNY72n8X9nS3I11pT0SI-yWNmzPAhyphenhyphen8DWokiz5O_JeXI0rz5adnzfFohYeK3dU7oGMMml-wqqrjpEremyqOR_tdbv8ta1QgX6aA0Jz2sBMoLWuKFuy2AoucgzBVWfJFNDmKc239m28pggTMWNo1IYcPtX4x7fVhJZEJ0zq7RV7Ow8G7A2c/s1843/2.png)

![screenshot](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiH9MpeqA-H-_C4SoYfsq-BAOV8Lx7VdZHfx4KJd8B0UpQKSktSUlqnQRcpvav6QZL3KUtABEX29s9yLjzePOgVS73PIhRo60JZhdHAlK-4OkTBBsVZo3TL2gdT41sPDuAAmVH2yjV0CXAVdnvjqZWKyt2s44a5kLBeZHRAKSjyMYuZHg9c4iMiZVcbRcw/s1860/3.png)

![screenshot](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgCGtHXnIRGeYEKwwGKKImRxQ5Rjxd-juY7lf25R76IjUBh2loOb9cIGOnxHbmkc5inW5HPVTsgWKysI3KAHSPmyEClepu8qV6fePmNkhJy-z2-55PuhUuXQZD-2Lc7YnoO7oSNcy9Ep3SUTZMWTwBzyYSzFCyqp60TIQPvwWZw4cGEkrOj-xJBsy96pg4/s1860/4.png)

![screenshot](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjJCHqJNINMGBZAmJJH30uV8Z0vRomu7UzWaUZXedMECeUoeG5i8dDsn48UihVFgzPxgkbBwdxoeYq5SO-dH0tdWiCBF4AoUXOnqtgB0ZRbvp5OBKcw3k27zjeh1AOi7iGIe5C0ES7Dm0h5mqmZG5afRVEUNeKoDzd-SXEptLFUOHQT3OFPu7Q4TV66AJg/s1860/5.png)

![screenshot](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgHwf0LxKjQ9WcRFY1M-y5jrSoXggjNfHMoygFYKEfl5SlrMVy1APNeXBWKhAC5mtpmao8fMNLnT3Shqf1D4LttPUWjjnAfqwXAhw7fYrT_j0AqFCbaoeZMRTDfLKbIWsw8Ac3REJFeIFc4vKObXhZY6DERYEpMPyOBegDI5ISWmOk7DVEcIDfL10hq-x8/s1860/6.png)

![screenshot](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhO5k0-xGXwsg_cqRY5uGVgU_1wg2hTLYjA7-SJzKoBOPwFDOdFxP2hQdcsq9UwonaK0jiIdzKvObz6AEhkZceVA1ox8SarLgbqFSbGeBWsN80EYrjXQ9ZP7SO9LaHUGmUbuT3dkoSBfzEHiMC5nRGWl1jE_u3rpr1t3HoFOc3EJCfTgER9Ok-ZmL5DrHo/s1860/7.png)

![screenshot](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjaTam7k8Jw3763nyaaksm2Hhs-k0yoP2lveo7m2473QfLJwv6Gfi23sNtwxb8EIo9HoGH4biqMMmjg6OiLEBGnj6n3W1rPACm2yWfyx8e6tpN6I4XhTMEacFMPo8xBBm_sSRKtrWhmAZrlwhgWi5wUn6NSohJrE6KmbbnBykTJFa87b0lJ9TnfcQQuTUE/s1860/8.png)

![screenshot](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjFoHRS1uBda4CdhAfcwRs0Lz570apwlTbuEPklqWhsYLu73ij8fKmIFbcUCLiWzf-UEjhe82_-J98QoPHirNY6HVkH5GjysTO2lmTnGYvbTIU3dRtXFfJuZVKoYV0I0_c9NPvW-DaRYCruGton-bWrd-YfvJzgzqwhuYHf8zTU7oEdP1aEjxzdGajmJkA/s1860/9.png)

![screenshot](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg0kCLnqcPV3G2vTGj17asVWdDhSyKfUuELJHG4bAkPeOhHsfedzIqR2WdlrhPNSSLwRBqxcJaVCoDV_dwlSMRlpxNh4meHXfv1mOdfZpu1JWW7PN2JJc7yOIh99SFng-b3n4A2Xq82WcILyemD0irBypFVcgg2QJ5RSPmZpnW85cYea_xQBkT5NRfzZI0/s1860/10.png)

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