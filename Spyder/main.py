# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 12:11:50 2021

@author: Administrator
"""

from flask import Flask, request, redirect, jsonify,send_file
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin
import matplotlib.pyplot as plt
from matplotlib.pyplot import pie, axis, show
from pymongo import MongoClient
import gridfs
import pandas
from bson.json_util import dumps
import tabula
import os
import csv
import urllib.request
from app import app
import glob
import os.path
import pandas as pd


@app.route('/file', methods=['POST','GET'])
@cross_origin()
def file():
	# check if the post request has the file part
	
	file = request.files['file']
	
	if file :
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['FOLDER'], filename))
		resp = jsonify({'message' : 'File successfully uploaded'})
		resp.status_code = 201
		return resp
	else:
		resp = jsonify({'message' : 'Allowed file types are pdf and csv only'})
		resp.status_code = 201
		return resp
    
@app.route("/graph", methods = ['GET','POST'])
def graph():
    target_path ='D:\\upload'

            

    folder_path = r'D:\\upload'
    file_type = '\*csv'
    files = glob.glob(folder_path + file_type)
    max_file = max(files, key=os.path.getctime)


    app = Flask(__name__)



    client = MongoClient('localhost:27017')
    db = client.image

    fs = gridfs.GridFS(db)



    x = []
    y = []

    import_file = pd.read_csv(max_file)
    print(import_file)
    print(max_file)
    with open(max_file,'r') as csvfile:
        plots = csv.reader(csvfile, delimiter = ',') 
        next(plots)
        for row in plots:
            x.append(row[0])
            y.append(row[1])

    fig = plt.figure()
    plt.bar(x, y, color = 'g', width = 0.5, label = "Transaction")
    plt.xlabel('Dates')
    plt.ylabel('Discription')
    plt.title('discription on spending money on date')
    plt.legend()
    plt.show()
    fig.savefig('D:\output\saved_figure.png')
    file = "saved_figure.png"
    return send_file("D:\output\saved_figure.png",mimetype=("image/png"))


@app.route("/graph1", methods = ['GET','POST'])
def graph1():
    target_path ='D:\\upload'
    folder_path = r'D:\\upload'
    file_type = '\*csv'
    files = glob.glob(folder_path + file_type)
    max_file = max(files, key=os.path.getctime)


    app = Flask(__name__)



    client = MongoClient('localhost:27017')
    db = client.image

    fs = gridfs.GridFS(db)



    x = []
    y = []

    import_file = pd.read_csv(max_file)
    print(import_file)
    print(max_file)
    with open(max_file,'r') as csvfile:
        plots = csv.reader(csvfile, delimiter = ',') 
        next(plots)
        for row in plots:
            x.append(row[0])
            y.append(row[4])

    fig = plt.figure()
    plt.bar(x, y, color = 'g', width = 0.5, label = "Age")
    plt.xlabel('Dates')
    plt.ylabel('Balance')
    plt.title('Balance of each date')
    plt.legend()
    plt.show()
    fig.savefig('D:\output1\saved_figure.png')
    file = "saved_figure.png"
    return send_file("D:\output1\saved_figure.png",mimetype=("image/png"))


@app.route("/graph2", methods = ['GET','POST'])
def graph2():
    target_path ='D:\\upload'
    folder_path = r'D:\\upload'
    file_type = '\*csv'
    files = glob.glob(folder_path + file_type)
    max_file = max(files, key=os.path.getctime)


    app = Flask(__name__)



    client = MongoClient('localhost:27017')
    db = client.image

    fs = gridfs.GridFS(db)



    x = []
    y = []

    import_file = pd.read_csv(max_file)
    print(import_file)
    print(max_file)
    with open(max_file,'r') as csvfile:
        plots = csv.reader(csvfile, delimiter = ',') 
        next(plots)
        for row in plots:
            x.append(row[3])
            y.append(row[1])

    fig = plt.figure()
    plt.bar(x, y, color = 'g', width = 0.5, label = "Age")
    plt.xlabel('Debit')
    plt.ylabel('Discription')
    plt.title('Discritption of each debit')
    plt.legend()
    plt.show()
    fig.savefig('D:\output2\saved_figure.png')
    file = "saved_figure.png"
    return send_file("D:\output2\saved_figure.png",mimetype=("image/png"))


@app.route("/graph3", methods = ['GET','POST'])
def graph3():
    target_path ='D:\\upload'
    folder_path = r'D:\\upload'
    file_type = '\*csv'
    files = glob.glob(folder_path + file_type)
    max_file = max(files, key=os.path.getctime)


    app = Flask(__name__)



    client = MongoClient('localhost:27017')
    db = client.image

    fs = gridfs.GridFS(db)



    x = []
    y = []

    import_file = pd.read_csv(max_file)
    print(import_file)
    print(max_file)
    with open(max_file,'r') as csvfile:
        plots = csv.reader(csvfile, delimiter = ',') 
        next(plots)
        for row in plots:
            x.append(row[0])
            y.append(row[3])

    fig = plt.figure()
    plt.bar(x, y, color = 'g', width = 0.5, label = "Age")
    plt.xlabel('Date')
    plt.ylabel('Debit')
    plt.title('Discritption of each debit')
    plt.legend()
    plt.show()
    fig.savefig('D:\output3\saved_figure.png')
    file = "saved_figure.png"
    return send_file("D:\output3\saved_figure.png",mimetype=("image/png"))





if __name__ == "__main__":
    app.run()