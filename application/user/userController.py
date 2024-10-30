from flask import request, session
from app import db, session_name, session_name_tmp
from application.user.userModel import User
from schemas import ValidateLoginSchema, ValidateAccountSchema, ValidateTokenSchema
import bcrypt, jwt
from app import JWT_SECRETKEY
from functions import send_success, send_warning, generatePassword, generateToken
from marshmallow import ValidationError

class UserController:
    
    def login(self):
        request_data = request.json
        schema = ValidateLoginSchema()
        try:
            result = schema.load(request_data)
                    
            username = result['username']
            password = result['password']
            
            user_db = User.query.filter(User.name == username).first()
            
            if user_db:
                if bcrypt.checkpw(password.encode('utf-8'),user_db.pwd.encode('utf-8')):
                    token = generateToken(user_db)
                    
                    session[session_name] = token
                    session[session_name_tmp] = username
                    
                    response = send_success('El usuario fue logeado correctamente', token)
                    return response
                else:
                    response = send_warning('La contraseña es incorrecta')
                    return response
            else:
                response = send_warning('El usuario no existe')
                return response
            
        except ValidationError as err:
            response = send_warning(err.messages)
            return response
                
    def account(self):
        request_data = request.json
        schema = ValidateAccountSchema()
        try:
            result = schema.load(request_data)
            username = result['username']
            new_username = result['new_username']
            password = result['password']
            new_password = result['new_password']
            
            user_db = User.query.filter(User.name == username).first()
            
            if user_db:
                if bcrypt.checkpw(password.encode('utf-8'),user_db.pwd.encode('utf-8')):
                    user_db.name = new_username
                    user_db.pwd = generatePassword(new_password)
                    try:
                        db.session.commit()
                        response = send_success('Los datos de la cuenta fueron actualizados correctamente')
                        return response
                    except:
                        response = send_warning('Ocurrío un error actualizado los datos de la cuenta')
                        return response
                else:
                    response = send_warning('La contraseña es incorrecta')
                    return response
            else:
                response = send_warning('El usuario no existe')
                return response
                        
        except ValidationError as err:
            response = send_warning(err.messages)
            return response
        
    def validate(self):
        request_data = request.json
        schema = ValidateTokenSchema()
        try:
            result = schema.load(request_data)
            token = result['token']
            
            try:
                data = jwt.decode(token, JWT_SECRETKEY, algorithms='HS256')
                return send_success('El token fue validado correctamente', data)
            except jwt.ExpiredSignatureError:
                return send_warning('El token es inválido')
            except jwt.InvalidTokenError:
                return send_warning('El token es inválido')
                        
        except ValidationError as err:
            response = send_warning(err.messages)
            return response