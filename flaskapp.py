from flask import Flask,render_template
'''
   It Creates an instance of Flask class5,
   which will be my WSGI (web server gateway application).
'''
##WSGI Application
app = Flask(__name__)

##creating route 
@app.route("/")
def welcome():
    return "<html><H1>Welcome to my Flask page</H1><html>"

##we can create multiple routes with different names
@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/form",methods=['GET','POST'])
def form():
    if request.method=="POST":
        name=request.form['name']
        return f'Hello {name}!'
    return render_template('about.html')

@app.route("/last")
def last():
    return "<html><P3>Thank you for visiting</P3><html>"

if __name__=="__main__":
    app.run(debug=True)



