from datetime import datetime, timezone, timedelta
import bcrypt, jwt
from app import JWT_SECRETKEY

def send_success(message, data = None):
    data = {
        'estado': 1,
        'mensaje': message,
        'datos': data
    }
    return data

def send_warning(message):
    data = {
        'estado': 0,
        'mensaje': message,
    }
    return data

def send_error():
    data = {
        'estado': 0,
        'mensaje': 'Ocurrió un error interno en el servidor',
    }
    return data

def generatePassword(pwd):
    result = bcrypt.hashpw(pwd.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    return result

def generateToken(user):
    
    token = jwt.encode(
        payload={
            'userId' : user.id,
            'userName' : user.name,
            'exp' : datetime.now(timezone.utc) + timedelta(minutes=1440)
        },
        key=JWT_SECRETKEY,
        algorithm='HS256'
    )
    
    return token