from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, select

import requests
import json
import datetime
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app)

#---------Connect Flask to database----------------#
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testdb.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

engine = create_engine('sqlite:///testdb.db')

#Connect to DB
connection = engine.connect()

metadata = MetaData()  #initialise metadata object

tasktable = Table("tasktable", metadata, autoload=True, autoload_with=engine)

#--------Generation of DB--------------------#

class Tasktable(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    title = db.Column('title', db.String)
    description = db.Column('description', db.String)
    important = db.Column('important', db.Integer)
    status = db.Column('status', db.Integer)
    date = db.Column('date', db.String)


#----------Select and print data from db-----------#

stmt = 'SELECT * from tasktable'
results_proxy = connection.execute(stmt)
results = results_proxy.fetchall()


#---------Taking user input from front end and ADDING  to db----------#
@app.route("/addtask")
def addtask():
    task_input = "welcome"
    all_tasks =  (', '.join(str(v) for v in results))
    return render_template("add_data.html",**locals())

#---------Display user added info on /complete route----------#

@app.route("/complete", methods = ["POST"])
def add_data():
    all_tasks =  (', '.join(str(v) for v in results))
    task_input = Tasktable(id=request.form["task_id"], title=request.form["task_title"], description=request.form["description"])
    db.session.add(task_input)
    db.session.commit()
    return render_template("add_data.html", **locals())

#---------Deletin from DB----------#
@app.route("/delete", methods = ["DELETE"])
def delete_data():
    task_input = Tasktable(id=request.form["task_id"], title=request.form["task_title"], description=request.form["description"])
    db.session.delete(task_input)
    db.session.commit()
    return render_template("remove_data.html", **locals())

#----Display ALL db data-------#

@app.route("/all_data")
def display_ALL_DATA():
    task_input = "ignore this but keep it!"
    all_tasks =  (', '.join(str(v) for v in results))
    return render_template("add_data.html", **locals())


#---------RN Other finctions  -------#

@app.route("/columns")
def display_columns():
    columns = table_columns()
    return render_template("index.html", **locals())







#----------------HIEN---------------#

@app.route('/todos',methods = ['GET','POST'])
def alltodos():
    if request.method == 'GET':
        return jsonify(todos)

    if request.method == 'POST':
        form_data = request.form
        result = request.form.getlist("checkbox")
        if result != []:
            result = 1
        else:
            result= 0
        todo = {
            'id' : todos[-1]['id'] + 1,
            'title' : form_data["task_title"],
            'description' : form_data["task_desc"],
            'important' : result,
            'status' : 0,
            'date' :form_data["due_date"]
        }
        todos.append(todo)
        return jsonify(todos)

#GET INDIVIUDAL TASK API

@app.route('/todos/<int:id>', methods=['DELETE'])
def delete_todo(id):
    todo =[todo for todo in todos if todo["id"]== id]
    todos.remove(todo[0])
    return jsonify(todos)


#@app.route('/todos/<int:id>', methods=['PUT'])
#def update_todo(id):
#    todo =[todo for todo in todos if todo["id"]== id]
#    todos.remove(todo[0])
#    return jsonify(todos)
#

@app.route("/", methods=['GET', 'POST'])
def index():
    #Datetime info for header
    now = datetime.datetime.now()
    current_date = now.strftime('%d-%m-%Y')
    current_time = now.strftime('%H:%M')
    current_month = now.strftime('%B')

    #Displaying specific greeting based on datetime info
    if now.hour < 12:
        greeting = 'good morning'
    elif now.hour >12 and now.hour < 17:
        greeting = 'good afternoon'
    else:
        greeting = 'good evening'

    #Displaying tasks in table
    url = 'http://127.0.0.1:5000/todos'
    response = requests.get(url)
    data = response.json()
    for item in data:
        if item['important'] == 0:
            importance = 'no'
        else:
            importance = 'yes'
    return render_template("index.html", **locals())

#---------HIEN JSON--------------------#
todos = [
        { "id": 0,
         "title": "First Task",
         "description": "this is the first description",
         "important": 0,
         "status": 0,
         "date": "01-01-2019"
         },

         {
         "id": 1,
         "title": "Second Task",
         "description": "this is the first description",
         "important": 0,
         "status": 0,
         "date": "03-02-2019"},

         {
         "id": 2,
         "title": "third Task",
         "description": "this is the third description",
         "important": 1,
         "status": 1,
         "date": "02-02-2019"},
        ]



#---------Databse TEST functions-------#
def check_db():
    try:
        print(engine.table_names())
        print(repr(tasktable))
        print("Database connected")
    except Exception as e:
        print(e)
check_db()


if __name__ == "__main__":
    app.run(debug=True)



# form_data = request.form
#     checkbox_result = request.form.getlist("checkbox")
#     print(result)
#     result2= "".join(result)
#     print (result2)
#     if result2 == "checked":
#         importance = "yes"
#     else:
#         importance = "no"
#     return render_template("index.html", **locals())
#     # important = form_data["extras"]
#     # if important == "checked":
#     #     importance = "yes"
#     # else:
#     #     importance = "no"
