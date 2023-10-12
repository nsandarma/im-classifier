from flask import Flask
from flask_restful import Resource,Api
app = Flask(__name__)
app.config['SECRET_KEY'] = '2024PrabowoMenang'

api =  Api(app)

from .routes import *
from .utils import *
from .rest import *
