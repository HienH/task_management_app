from flask import Flask, render_template, request
from classes_db import *

app = Flask(__name__)


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
