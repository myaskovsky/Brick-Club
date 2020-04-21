import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from flask_bcrypt import Bcrypt
#from flask_login import LoginManager
#from flask_mail import Mail


app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'


db = SQLAlchemy(app) #init


from app.main.routes import main
from app.users.routes import users

app.register_blueprint(main)
app.register_blueprint(users)

