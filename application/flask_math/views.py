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
        return render_template("derivative.html",formula=formula,a=a,anser_0=anser[0],anser_1=anser[1],anser_2=anser[2],anser_3=anser[3])
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


@view.route("/base_conversion",methods=["GET","POST"])
def  base_conversion_view():
    if request.method=="POST":
        try:
            if request.form.get("bin")!="":
                base="binary"
                before_conversion=request.form.get("bin")
            elif request.form.get("oct")!="":
                base="octal"
                before_conversion=request.form.get("oct")
            elif request.form.get("dec")!="":
                base="decimal"
                before_conversion=request.form.get("dec")
            elif request.form.get("hex")!="":
                base="hexadecimal"
                before_conversion=request.form.get("hex")
            anser=base_conversion.base_conversion(base,before_conversion)
        except:
            anser=["Error","Error","Error","Error"]
            flash("エラー：もう一度入力してください")
        return render_template("base_conversion.html",bin=anser[0],oct=anser[1],dec=anser[2],hex=anser[3])
    else:
        return render_template("base_conversion.html")


@view.route("/Factorial",methods=["GET","POST"])
def  Factorial_view():
    if request.method=="POST":
        formula=request.form.get("formula")
        anser=Factorial.Factorial(formula)
        return render_template("Factorial.html",formula=formula,anser=anser)
    else:
        return render_template("Factorial.html")



@view.route("/equation",methods=["GET","POST"])
def  equation_view():
    if request.method=="POST":
        formula=request.form.get("formula")
        Anser=equation.equation(formula)
        return render_template("equation.html",formula=formula,Anser=Anser)
    else:
        return render_template("equation.html")


@view.route("/BMI",methods=["GET","POST"])
def  BMI_view():
    if request.method=="POST":
        height=request.form.get("height")
        weight=request.form.get("weight")
        anser=BMI.BMI(height,weight)
        return render_template("BMI.html",height=height,weight=weight,anser_0=anser[0],anser_1=anser[1])
    else:
        return render_template("BMI.html")


@view.app_errorhandler(404)
def non_existant_route(error):
    flash("404 NOT FOUND")
    return redirect(url_for("view.index_view"))
