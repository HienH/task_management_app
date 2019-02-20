from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, select

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

# tasktable = Table("tasktable", metadata, autoload=True, autoload_with=engine)

#--------Generation of DB--------------------#

class Tasktable(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    title = db.Column('title', db.String)
    description = db.Column('description', db.String)
    important = db.Column('important', db.Integer)
    status = db.Column('status', db.Integer)
    date = db.Column('date', db.String)


#---------Database Add/remove/print data functions -------#

stmt = 'SELECT * from mytable'
results_proxy = connection.execute(stmt)
results = results_proxy.fetchall()

def table_columns():
    columns = results[0].keys()
    #print(columns)
    return columns


def print_tasks():
    first_row = results[0]
    return first_row

#--------- FLASK -------#

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/columns")
def display_columns():
    columns = table_columns()
    return render_template("index.html", **locals())

#---------Taking user input from front end and adding to db----------#
@app.route("/addtask")
def addtask():
    return render_template("add_data.html")

#---------Display user added info on /complete route----------#
@app.route("/complete", methods = ["POST"])
def add_data():
    task_input = Tasktable(id=request.form["task_id"], title=request.form["task_title"], description=request.form["description"])
    db.session.add(task_input)
    db.session.commit()
    return render_template("add_data.html", **locals())
# print(result)
#add_data()

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
            'data' :form_data["due_date"]
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




#---------HIEN JSON--------------------#
todos = [
        { "id": 0,
         "title": "First Task",
         "description": "this is the first description",
         "important": 0,
         "status": 0,
         "date": "01-01-2019"
         }, {
         "id": 1,
         "title": "First Task",
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
