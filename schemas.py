from marshmallow import Schema, fields

class ValidateLoginSchema(Schema):
    username = fields.String(required=True)
    password = fields.String(required=True)
    
class ValidateProcessSchema(Schema):
    name = fields.String(required=True)
    url = fields.String(required=True)
    timeout = fields.Integer(required=True) 
    
class ValidateTaskSchema(Schema):
    name = fields.String(required=True)
    directory = fields.String(required=True)
    command = fields.String(required=True)
    process_id = fields.Integer(required=True)
    
class ValidateAccountSchema(Schema):
    username = fields.String(required=True)
    new_username = fields.String(required=True)
    password = fields.String(required=True)
    new_password = fields.String(required=True)
    
class ValidateTokenSchema(Schema):
    token = fields.String(required=True)