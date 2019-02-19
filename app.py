
from database import *
import datetime
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

#---------Connect Flask to database----------------#
app.config['SQLALCHEMY_DATABASE URI'] = 'sqlite:////c/Users/RN/FINAL_PROJECTS/task_management_app/taskdatabase.db'

# db = sqlalchemy(app)


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
            'data' :"01-02-99"
        }
        todos.append(todo)
        return jsonify(todos)


#GET INDIVIUDAL TASK API

@app.route('/todos/<int:id>',methods = ['GET'])
def get_todo(id):
    for todo in todos:
        if(id == todo["id"]):
            return jsonify(todo),200
    return "Todo not found",404



@app.route("/")
def index():
    now = datetime.datetime.now()
    todays_date = now.strftime('%d-%m-%Y')
    todays_time = now.strftime('%H:%M')
    if now.hour < 12:
        greeting = 'good morning'
    elif now.hour >=12 and now.hour < 17:
        greeting = 'good afternoon'
    else:
        greeting = 'good evening'
    return render_template("index.html", **locals())


#@app.route("/taskadded", methods = ["POST"])
#def add_task():
#
#
#
#    return render_template("index.html", **locals())
#    # important = form_data["extras"]
#    # if important == "checked":
#    #     importance = "yes"
#    # else:
#    #     importance = "no"
#    #
#



if __name__ == "__main__":
    app.run(debug=True)
