from flask import request, redirect, url_for, render_template, flash, session
from flask import current_app as app
from flask_math.calculation import *
from flask import Blueprint
from sympy import *

view=Blueprint("view",__name__)

@view.route("/")
def index_view():
    return render_template("index.html")


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


@view.route("/BMI",methods=["GET","POST"])
def  BMI_view():
    if request.method=="POST":
        height=request.form.get("height")
        weight=request.form.get("weight")
        anser=BMI.BMI(height,weight)
        return render_template("BMI.html",height=height,weight=weight,anser_0=anser[0],anser_1=anser[1])
    else:
        return render_template("BMI.html")


@view.route("/derivative",methods=["GET","POST"])
def  derivative_view():
    if request.method=="POST":
        formula=request.form.get("formula")
        type=request.form.get("type")
        anser=derivative.derivative(formula,type)
        return render_template("derivative.html",formula=formula,type=type,anser_0=anser[0],anser_1=anser[1],anser_2=anser[2],anser_3=anser[3])
    else:
        return render_template("derivative.html")


@view.route("/equation",methods=["GET","POST"])
def  equation_view():
    if request.method=="POST":
        formula=request.form.get("formula")
        Anser=equation.equation(formula)
        return render_template("equation.html",formula=formula,Anser=Anser)
    else:
        return render_template("equation.html")


@view.route("/equations",methods=["GET","POST"])
def  equations_view():
    if request.method=="POST":
        try:
            number=int(request.form.get("number"))
            if number>=1 and number<=3:
                return render_template("equations_2.html",number=number)
            else:
                flash("エラー:3以下の自然数を入力してください")
                return render_template("equations.html")
        except:
            flash("エラー：もう一度入力してください")
            return render_template("equations.html")
    else:
        return render_template("equations.html")


@view.route("/equations_2",methods=["GET","POST"])
def  equations_2_view():
    if request.method=="POST":
        number=request.form.get("number")
        if number=="1":
            formula_1=request.form.get("formula_1")
            Formula=[formula_1]
            anser=equations.equations(Formula)
            return render_template("equations_2.html",formula_1=formula_1,anser=anser,number=int(number))
        elif number=="2":
            formula_1=request.form.get("formula_1")
            formula_2=request.form.get("formula_2")
            Formula=[formula_1,formula_2]
            anser=equations.equations(Formula)
            return render_template("equations_2.html",formula_1=formula_1,formula_2=formula_2,anser=anser,number=int(number))
        elif number=="3":
            formula_1=request.form.get("formula_1")
            formula_2=request.form.get("formula_2")
            formula_3=request.form.get("formula_3")
            Formula=[formula_1,formula_2,formula_3]
            anser=equations.equations(Formula)
            return render_template("equations_2.html",formula_1=formula_1,formula_2=formula_2,formula_3=formula_3,anser=anser,number=int(number))
    else:
        return render_template("equations_2.html")


@view.route("/Factorial",methods=["GET","POST"])
def  Factorial_view():
    if request.method=="POST":
        formula=request.form.get("formula")
        anser=Factorial.Factorial(formula)
        return render_template("Factorial.html",formula=formula,anser=anser)
    else:
        return render_template("Factorial.html")


@view.route("/factorization",methods=["GET","POST"])
def  factorization_view():
    if request.method=="POST":
        formula=request.form.get("formula")
        anser=factorization.factorization(formula)
        return render_template("factorization.html",formula=formula,anser=anser)
    else:
        return render_template("factorization.html")


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


@view.route("/lim",methods=["GET","POST"])
def  lim_view():
    if request.method=="POST":
        formula=request.form.get("formula")
        a=request.form.get("a")
        anser=lim.lim(formula,a)
        return render_template("lim.html",formula=formula,a=a,anser_1=anser[0],anser_2=anser[1])
    else:
        return render_template("lim.html",a=0)


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


@view.app_errorhandler(404)
def non_existant_route(error):
    flash("404 NOT FOUND")
    return redirect(url_for("view.index_view"))






@view.route("/matrix",methods=["GET","POST"])
def  matrix_view():
    if request.method=="POST":
        Ar=int(request.form.get("Ar"))
        Ac=int(request.form.get("Ac"))
        matrixA=str(request.form.get("matrix"))

        matrixA_list=list(matrixA)
        List=[]
        for k in range(Ar):
            List.append([])

        for j in range(0,Ar,1):
            for i in range(j*(3*Ac+1),(j+1)*(3*Ac+1)-3,3):
                if matrixA_list[i]==" ":
                    m=int(matrixA_list[i+1])
                else:
                    m=-int(matrixA_list[i+1])
                List[j].append(m)

        A=Matrix(List)

        type=int(request.form.get("type"))
        Anser=matrix.calculation(A,Ar,Ac,type)
        if Anser[4]==0:
            anser=[]
            for i in range(Anser[1]):
                A=str(Anser[0].row(i))
                A=A.replace("Matrix","").replace("**","^").replace("*","").replace("([[","[").replace("]])","]")
                anser.append(A)
        elif Anser[4]==1:
            anser=[Anser[0]]
        return render_template("matrix.html",matrix=matrixA,Ar=Ar,Ac=Ac,anser_0=anser,anser_3=Anser[3])
    else:
        return render_template("matrix.html",Ar=2,Ac=2)


@view.route("/matrix_2",methods=["GET","POST"])
def  matrix_2_view():
    if request.method=="POST":
        Ar=int(request.form.get("Ar"))
        Ac=int(request.form.get("Ac"))
        matrixA=str(request.form.get("matrixA"))

        matrixA_list=list(matrixA)
        List_A=[]
        for k in range(Ar):
            List_A.append([])

        for j in range(0,Ar,1):
            for i in range(j*(3*Ac+1),(j+1)*(3*Ac+1)-3,3):
                if matrixA_list[i]==" ":
                    m=int(matrixA_list[i+1])
                else:
                    m=-int(matrixA_list[i+1])
                List_A[j].append(m)

        A=Matrix(List_A)


        Br=int(request.form.get("Br"))
        Bc=int(request.form.get("Bc"))
        matrixB=str(request.form.get("matrixB"))

        matrixB_list=list(matrixB)
        List_B=[]
        for k in range(Br):
            List_B.append([])

        for j in range(0,Br,1):
            for i in range(j*(3*Bc+1),(j+1)*(3*Bc+1)-3,3):
                if matrixB_list[i]==" ":
                    m=int(matrixB_list[i+1])
                else:
                    m=-int(matrixB_list[i+1])
                List_B[j].append(m)

        B=Matrix(List_B)

        type=int(request.form.get("type"))
        k=request.form.get("k")
        l=request.form.get("l")
        Anser=matrix_2.calculation(A,B,Ar,Ac,Br,Bc,type,k,l)
        anser=[]
        for i in range(Anser[2]):
            A=str(Anser[0].row(i))
            A=A.replace("Matrix","").replace("**","^").replace("*","").replace("([[","[").replace("]])","]")
            anser.append(A)
        return render_template("matrix_2.html",matrixA=matrixA,matrixB=matrixB,Ar=Ar,Ac=Ac,Br=Br,Bc=Bc,k=k,l=l,anser_0=anser,anser_1=Anser[1])
    else:
        return render_template("matrix_2.html",Ar=2,Ac=2,Br=2,Bc=2,k=2,l=2)
