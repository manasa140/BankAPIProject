# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 10:09:26 2021

@author: Administrator
"""
from flask import Flask
from flask_cors import CORS, cross_origin
FOLDER = 'D:/upload'

app = Flask(__name__)
app.secret_key = "secret key"
app.config['FOLDER'] = FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
