##Building url dynamically
##variable rule
##JINJA2 Template in Flask

from flask import Flask,render_template,request
app = Flask(__name__)
@app.route("/")
def welcome():
    return "<html><H1>Welcome to my Flask page</H1><html>"

@app.route("/form",methods=['GET','POST'])
def form():
    if request.method=="POST":
        name=request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')

##variable rule

@app.route("/success/<int:score>")
def success(score):
    return "The marks you got is"+ str(score)


if __name__=="__main__":
    app.run(debug=True)


