from flask import request, session, redirect
from functools import wraps
import jwt
from app import JWT_SECRETKEY, session_name
from functions import send_warning

def AuthBack(*options, **default_kwargs):

    def wrapper(view_func):
        @wraps(view_func)
        def view(*args, **kwargs):
                                    
            result = view_func(*args, **kwargs)
                        
            headers = request.headers
            bearer = headers.get('Authorization')
            token = bearer.split()[1]
                        
            if not token:
                return send_warning('Acceso denegado'), 403
            try:
                jwt.decode(token, JWT_SECRETKEY, algorithms='HS256')
            except jwt.ExpiredSignatureError:
                return send_warning('Acceso denegado'), 403
            except jwt.InvalidTokenError:
                return send_warning('Acceso denegado'), 403
            
            return result 

        return view

    return wrapper

def isAuth():
    if not session.get(session_name):
        return False
    token = session.get(session_name)
    try:
        jwt.decode(token, JWT_SECRETKEY, algorithms='HS256')
        return True
    except jwt.ExpiredSignatureError:
        return False
    except jwt.InvalidTokenError:
        return False