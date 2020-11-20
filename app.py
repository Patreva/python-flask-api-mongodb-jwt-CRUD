from flask import Flask
from flask_restful import Api
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from resources.errors import errors
from os import environ
from flask_mail import Mail

from database.db import initialize_db


app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = environ.get('JWT_SECRET_KEY')
app.config['MAIL_SERVER'] = environ.get('MAIL_SERVER')
app.config['MAIL_PORT'] = environ.get('MAIL_PORT')
app.config['MAIL_USERNAME'] = environ.get('MAIL_USERNAME')

api = Api(app)

api = Api(app, errors=errors)

bcrypt = Bcrypt(app)

jwt = JWTManager(app)

mail = Mail(app)

# imports requiring app and mail
from resources.routes import initialize_routes

CONNECTION_STRING = ''

app.config['MONGODB_SETTINGS'] = {
    'host': CONNECTION_STRING
}

initialize_db(app)

initialize_routes(api)
