from app import app
from flask import render_template, request
from app.models import model, formopener

@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
   return render_template("index.html")



@app.route('/results', methods=['GET', 'POST'])
@app.route('/results.html', methods=['GET', 'POST'])
def startAdven():
    if request.method == 'GET':
        return "Sorry, your story is over."
    else:
        userdata = request.form
        name = (userdata["userName"]).capitalize()
    return render_template("/results.html", name = name)



@app.route('/decision', methods=['GET', 'POST'])
@app.route('/decision.html', methods=['GET', 'POST'])
def nextAdven():
   if request.method == 'GET':
       return "Sorry, your story is over."
   else:
        userdata = request.form
        x = (userdata["decision"])
        if x == "option01":
           return render_template("/wrong.html", x=x)   
        elif x == "option02":
            return render_template("/results2.html", x=x)
        elif x == "option03":
            return render_template("/results3.html", x=x)
        elif x == "option04":
            return render_template("/results4.html", x=x)

#From results3 to 7 or 8

@app.route('/decision3b', methods=['GET', 'POST'])
@app.route('/decision3b.html', methods=['GET', 'POST'])
def nextAdvenghgfg():
   if request.method == 'GET':
       return "Sorry, your story is over."
   else:
        userdata = request.form
        x = (userdata["decision"])
        if x == "option01":
           return render_template("/wrong.html", x=x)   
        elif x == "option02":
            return render_template("/results7.html", x=x)
        elif x == "option03":
            return render_template("/results8.html", x=x)

#From results4 to 9 or 10

@app.route('/decision4c', methods=['GET', 'POST'])
@app.route('/decision4c.html', methods=['GET', 'POST'])
def nextAdvenghgshfg():
   if request.method == 'GET':
       return "Sorry, your story is over."
   else:
        userdata = request.form
        x = (userdata["decision"])
        if x == "option01":
           return render_template("/wrong.html", x=x)   
        elif x == "option02":
            return render_template("/results9.html", x=x)
        elif x == "option03":
            return render_template("/results10.html", x=x)


