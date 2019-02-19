
from database import *
from flask import Flask, render_template, request,jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

#---------Connect Flask to database----------------#
app.config['SQLALCHEMY_DATABASE URI'] = 'sqlite:///taskmanager.db'

# db = sqlalchemy(app)

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

@app.route("/")
def index():
    return render_template("index.html")
    
 
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

