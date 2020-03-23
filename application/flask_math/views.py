from flask import request, redirect, url_for, render_template, flash, session
from flask_math import app
from flask_math.math import integral, derivative

@app.route("/")
def show_entries():
    return render_template("index.html")

@app.route("/integral",methods=["GET","POST"])
def  integral_view():
    if request.method=="POST":
        formula=request.form.get("formula")
        anser=integral(formula)
        return render_template("integral.html",anser=anser)
    else:
        return render_template("integral.html")


@app.route("/derivative",methods=["GET","POST"])
def  derivative_view():
    if request.method=="POST":
        formula=request.form.get("formula")
        anser=derivative(formula)
        return render_template("derivative.html",anser=anser)
    else:
        return render_template("derivative.html")
