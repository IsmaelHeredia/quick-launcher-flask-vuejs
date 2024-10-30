from app import app
from app import db
from application.user.userModel import User

from functions import generatePassword

@app.cli.command()
def seed():
    
    user = User(name='admin', pwd=generatePassword('admin'))
    
    db.session.add(user)
    db.session.commit()
        
    print('Database seeded')