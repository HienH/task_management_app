from flask import Flask, render_template, request
from classes_db import *

app = Flask(__name__)

<<<<<<< HEAD
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
=======

@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/taskadded", methods = ["POST"])
def add_task():
    form_data = request.form
    task = form_data["task_title"]
    task_desc = form_data["task_desc"]
    result = request.form.getlist("checkbox")
    print(result)
    result2= "".join(result)
    print (result2)
    if result2 == "checked":
        importance = "yes"
    else:
        importance = "no"
    return render_template("index.html", **locals()) 
    # important = form_data["extras"]
    # if important == "checked":
    #     importance = "yes"
    # else:
    #     importance = "no"
    #    



if __name__ == "__main__":
    app.run(debug=True)
>>>>>>> be1d38eafd9487c67e7b95c82500f4932de745ae
