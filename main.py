from flask import Flask
from flask_restplus import Api,Resource,fields
from flask_cors import CORS

app = Flask(__name__)
api = Api(app, version='1.0',title='MPESA API',
            description='mpesa api covering STK push and C2B')
CORS(app)

from resources.stkpush import *
from resources.c2b import *
