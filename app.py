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


def __init__(self, id, title, description, important, status, date):
    self.id = id
    self.title = title
    self.description = description
    self.important = important
    self.status = status
    self.date = date

#----------Select and print data from db-----------#

# stmt = 'SELECT * from tasktable'
# results_proxy = connection.execute(stmt)
# results = results_proxy.fetchall()

#---------Display ALL data -------#
def display_all():
    connection = engine.connect()
    stmt = 'SELECT * from tasktable'
    results_proxy = connection.execute(stmt)
    results = results_proxy.fetchall()
    return results
#---------Taking user input from front end and ADDING  to db----------#
@app.route("/")
def addtask():
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
    results = display_all()
    # for row in results:
    #     print(row)
    return render_template("RNindex.html",**locals())

#---------Display user added info on /complete route----------#

@app.route("/added", methods = ["POST"])
def add_tasks():
    task_input = Tasktable(id=request.form["task_id"], title=request.form["task_title"], description=request.form["task_description"], important=request.form["checkbox"], status=request.form["status"], date=request.form["task_date"])
    db.session.add(task_input)
    db.session.commit()
    results = display_all()
    return render_template("RNindex.html", **locals())

   

#---------Deletin from DB----------#
@app.route("/deleted", methods = ["POST"])
def delete_data():
    deleteme = Tasktable.query.filter_by(id=request.form["task_id"]).first()
    db.session.delete(deleteme)
    db.session.commit()
    results = display_all()
    return render_template("RNindex.html", **locals())


# #----ADD/UPDATE/DELET from database -------#

# @app.route("/all_data")
# def display_ALL_DATA():
#     task_input = "ignore this but keep it!"
#     all_tasks =  (', '.join(str(v) for v in results))
#     return render_template("add_data.html", **locals())

def add_data():
    addme = Tasktable(id=1,title=("firstid"), description="randomdesc", important=0, status=0, date="a date")
    db.session.add(addme)
    db.session.commit()

#add_data()   


#delete_data(5)

def update_data(id):
    updateme = Tasktable.query.filter_by(id=id).first()
    updateme.title = "changed"
    db.session.commit()
  


#display_all()


#---------Databse TEST functions-------#
def check_db():
    try:
        print(engine.table_names())
        print(repr(tasktable))
        print("Database connected")
    except Exception as e:
        print(e)
#check_db()







#GET INDIVIUDAL TASK API






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
