#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 14:44:14 2019

@author: hienh
"""

from flask import Flask,render_template,request,make_response,jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)


@app.route('/')
def todos():
    if request.method == 'GET':
        todos = [
        { "id": 0,
         "title": "First Task",
         "description": "this is the first description",
         "important": 0,
         "status": 0,
         "date": "01-01-2019"
         }, {
         "id": 0,
         "title": "First Task",
         "description": "this is the first description",
         "important": 0,
         "status": 0,
         "date": "01-01-2019"},
        ]
        return jsonify(todos)
   
if __name__ == '__main__':
    app.run(debug =True)
