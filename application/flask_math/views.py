from flask import request, redirect, url_for, render_template, flash, session
from flask_math import app
from flask_math.math import integral, derivative, taylor

@app.route("/")
def index_view():
    return render_template("index.html")

@app.route("/integral",methods=["GET","POST"])
def  integral_view():
    if request.method=="POST":
        formula=request.form.get("formula")
        anser=integral(formula)
        return render_template("integral.html",formula=formula,anser=anser)
    else:
        return render_template("integral.html")


@app.route("/derivative",methods=["GET","POST"])
def  derivative_view():
    if request.method=="POST":
        formula=request.form.get("formula")
        anser=derivative(formula)
        return render_template("derivative.html",formula=formula,anser=anser)
    else:
        return render_template("derivative.html")


@app.route("/taylor",methods=["GET","POST"])
def  taylor_view():
    if request.method=="POST":
        formula=request.form.get("formula")
        a=request.form.get("a")
        b=request.form.get("b")
        anser=taylor(formula,a,b)
        return render_template("taylor.html",formula=formula,anser=anser,a=a,b=b)
    else:
        return render_template("taylor.html")
