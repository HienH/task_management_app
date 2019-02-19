from flask import Flask, render_template, request
from classes_db import *

app = Flask(__name__)

app = Flask(__name__)
cors = CORS(app)

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
