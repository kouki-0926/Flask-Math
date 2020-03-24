from flask import request, redirect, url_for, render_template, flash, session
from flask import current_app as app
from flask_math.math import integral, derivative, taylor ,lim
from flask import Blueprint

view=Blueprint("view",__name__)

@view.route("/")
def index_view():
    return render_template("index.html")

@view.route("/integral",methods=["GET","POST"])
def  integral_view():
    if request.method=="POST":
        formula=request.form.get("formula")
        anser=integral(formula)
        return render_template("integral.html",formula=formula,anser=anser)
    else:
        return render_template("integral.html")


@view.route("/derivative",methods=["GET","POST"])
def  derivative_view():
    if request.method=="POST":
        formula=request.form.get("formula")
        anser=derivative(formula)
        return render_template("derivative.html",formula=formula,anser=anser)
    else:
        return render_template("derivative.html")


@view.route("/taylor",methods=["GET","POST"])
def  taylor_view():
    if request.method=="POST":
        formula=request.form.get("formula")
        a=request.form.get("a")
        b=request.form.get("b")
        anser=taylor(formula,a,b)
        return render_template("taylor.html",formula=formula,anser=anser,a=a,b=b)
    else:
        return render_template("taylor.html")


@view.route("/limit",methods=["GET","POST"])
def  limit_view():
    if request.method=="POST":
        formula=request.form.get("formula")
        a=request.form.get("a")
        anser=lim(formula,a)
        return render_template("limit.html",formula=formula,anser_1=anser[0],anser_2=anser[1],a=a)
    else:
        return render_template("limit.html")


@view.app_errorhandler(404)
def non_existant_route(error):
    return redirect(url_for("view.index_view"))        
