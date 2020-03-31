from flask import request, redirect, url_for, render_template, flash, session
from flask import current_app as app
from flask_math.calculation import *
from flask import Blueprint

view=Blueprint("view",__name__)

@view.route("/")
def index_view():
    return render_template("index.html")

@view.route("/integral",methods=["GET","POST"])
def  integral_view():
    if request.method=="POST":
        formula=request.form.get("formula")
        upper_end=request.form.get("upper_end")
        lower_end=request.form.get("lower_end")
        type=request.form.get("type")
        anser=integral.integral(formula,upper_end,lower_end,type)
        return render_template("integral.html",formula=formula,upper_end=upper_end,lower_end=lower_end,type=type,anser=anser)
    else:
        return render_template("integral.html",type=0)


@view.route("/derivative",methods=["GET","POST"])
def  derivative_view():
    if request.method=="POST":
        formula=request.form.get("formula")
        a=request.form.get("a")
        anser=derivative.derivative(formula,a)
        return render_template("derivative.html",formula=formula,a=a,anser_0=anser[0],anser_1=anser[1],anser_2=anser[2])
    else:
        return render_template("derivative.html",a="x")


@view.route("/taylor",methods=["GET","POST"])
def  taylor_view():
    if request.method=="POST":
        formula=request.form.get("formula")
        dimension=request.form.get("dimension")
        center=request.form.get("center")
        anser=taylor.taylor(formula,dimension,center)
        return render_template("taylor.html",formula=formula,dimension=dimension,center=center,anser=anser)
    else:
        return render_template("taylor.html",dimension=10,center=0)


@view.route("/limit",methods=["GET","POST"])
def  limit_view():
    if request.method=="POST":
        formula=request.form.get("formula")
        a=request.form.get("a")
        anser=lim.lim(formula,a)
        return render_template("limit.html",formula=formula,anser_1=anser[0],anser_2=anser[1],a=a)
    else:
        return render_template("limit.html",a=0)


@view.app_errorhandler(404)
def non_existant_route(error):
    return redirect(url_for("view.index_view"))
