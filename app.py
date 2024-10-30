from flask import Flask, session
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_session import Session

import bcrypt

import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

app.debug = True

CORS(app)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

Session(app)

MYSQL = {
    'user':os.environ.get('DB_USERNAME'),
    'pwd':os.environ.get('DB_PASSWORD'),
    'db':os.environ.get('DB_DATABASE'),
    'host': os.environ.get('DB_HOST'),
    'port':os.environ.get('DB_PORT')
}

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://%(user)s:%(pwd)s@%(host)s:%(port)s/%(db)s' % MYSQL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

migrate = Migrate(app,db)

JWT_SECRETKEY = bcrypt.hashpw(os.environ.get('SECRET_KEY').encode('utf-8'), bcrypt.gensalt())

session_name = os.environ.get('SESSION_NAME')
session_name_tmp = os.environ.get('SESSION_NAME_TMP')

session_theme = os.environ.get('SESSION_THEME')

with app.app_context():
    from commands import *