#Building url dynamically
from flask import Flask,render_template,request,redirect
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

@app.route("/success/int:score")
def success(score):
    res=""
    if score>=50:
        res="Pass"
    else:
        res="Fail"
    return render_template('result.html')

@app.route("/successres/int:score")
def success(score):
    res=""
    if score>=50:
        res="Pass"
    else:
        res="Fail"
    exp={'score':score,'res':res}

    return render_template('result.html',result=res)


@app.route("/fail/int:score")
def fail(score):
    
    return render_template('result.html',result=score)


@app.route("/submit",methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=="POST":
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        AI=float(request.form['AI'])
        DS=float(request.form['DS'])

        total_score=(science+maths+AI+DS)
    return redirect(url_for('successres',score=total_score))
                                                          

if __name__=="__main__":
    app.run(debug=True)

