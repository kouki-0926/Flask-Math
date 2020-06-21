from flask import request, redirect, url_for, render_template, flash, Blueprint
from flask_math.calculation import *
from sympy import *

view=Blueprint("view",__name__)

@view.route("/")
def index_view():
    return render_template("index.html")


@view.route("/instructions")
def instructions_view():
    return render_template("instructions.html")


@view.route("/base_conversion",methods=["GET","POST"])
def base_conversion_view():
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
            flash("エラー：もう一度入力してくださいｔ")
        return render_template("base_conversion.html",bin=anser[0],oct=anser[1],dec=anser[2],hex=anser[3])
    else:
        return render_template("base_conversion.html")


@view.route("/BMI",methods=["GET","POST"])
def BMI_view():
    if request.method=="POST":
        height=request.form.get("height")
        weight=request.form.get("weight")
        anser=BMI.BMI(height,weight)
        return render_template("BMI.html",height=height,weight=weight,anser_0=anser[0],anser_1=anser[1])
    else:
        return render_template("BMI.html")


@view.route("/derivative",methods=["GET","POST"])
def derivative_view():
    if request.method=="POST":
        formula=request.form.get("formula")
        type=request.form.get("type")
        anser=derivative.derivative(formula,type)
        return render_template("derivative.html",
        formula=formula,type=type,anser_0=anser[0],anser_1=anser[1],anser_2=anser[2],anser_3=anser[3])
    else:
        return render_template("derivative.html",type="x")


@view.route("/equation",methods=["GET","POST"])
def equation_view():
    if request.method=="POST":
        formula=request.form.get("formula")
        Anser=equation.equation(formula)
        return render_template("equation.html",formula=formula,Anser=Anser)
    else:
        return render_template("equation.html")


@view.route("/equations",methods=["GET","POST"])
def equations_view():
    return render_template("equations.html")


@view.route("/equations_2",methods=["GET","POST"])
def equations_2_view():
    try:
        if request.method=="GET":
            number=int(request.args.get("number"))
            if number>=1 and number<=3:
                return render_template("equations_2.html",number=number)
            else:
                flash("エラー:3以下の自然数を入力してください")
                return redirect(url_for("view.equations_view"))

        elif request.method=="POST":
            number=int(request.form.get("number"))
            if number==1:
                formula_1=request.form.get("formula_1")
                Formula=[formula_1]
                Anser=equations.equations(Formula)
                return render_template("equations_2.html",formula_1=formula_1,Anser=Anser,number=number)
            elif number==2:
                formula_1=request.form.get("formula_1")
                formula_2=request.form.get("formula_2")
                Formula=[formula_1,formula_2]
                Anser=equations.equations(Formula)
                return render_template("equations_2.html",formula_1=formula_1,formula_2=formula_2,Anser=Anser,number=number)
            elif number==3:
                formula_1=request.form.get("formula_1")
                formula_2=request.form.get("formula_2")
                formula_3=request.form.get("formula_3")
                Formula=[formula_1,formula_2,formula_3]
                Anser=equations.equations(Formula)
                return render_template("equations_2.html",
                formula_1=formula_1,formula_2=formula_2,formula_3=formula_3,Anser=Anser,number=number)
            else:
                flash("エラー")
                return redirect(url_for("view.equations_view"))
    except:
        flash("エラー:もう一度入力してください")
        return redirect(url_for("view.equations_view"))


@view.route("/Euclidean_Algorithm",methods=["GET","POST"])
def Euclidean_Algorithm_view():
    if request.method=="POST":
        number_x=request.form.get("number_x")
        number_y=request.form.get("number_y")
        anser=Euclidean_Algorithm.Euclidean_Algorithm(number_x,number_y)
        return render_template("Euclidean_Algorithm.html",number_x=number_x,number_y=number_y,anser=anser)
    else:
        return render_template("Euclidean_Algorithm.html")


@view.route("/Expand",methods=["GET","POST"])
def Expand_view():
    if request.method=="POST":
        formula=request.form.get("formula")
        anser=Expand.Expand(formula)
        return render_template("Expand.html",formula=formula,anser=anser)
    else:
        return render_template("Expand.html")


@view.route("/Factorial",methods=["GET","POST"])
def Factorial_view():
    if request.method=="POST":
        formula=request.form.get("formula")
        anser=Factorial.Factorial(formula)
        return render_template("Factorial.html",formula=formula,anser=anser)
    else:
        return render_template("Factorial.html")


@view.route("/factorization",methods=["GET","POST"])
def factorization_view():
    if request.method=="POST":
        formula=request.form.get("formula")
        anser=factorization.factorization(formula)
        return render_template("factorization.html",formula=formula,anser=anser)
    else:
        return render_template("factorization.html")


@view.route("/graph",methods=["GET","POST"])
def graph_view():
    if request.method=="POST":
        formula=request.form.get("formula")
        lower_end=request.form.get("lower_end")
        upper_end=request.form.get("upper_end")
        title=request.form.get("title")
        graph.graph(formula,lower_end,upper_end,title)
        return render_template("graph.html",formula=formula,lower_end=lower_end,upper_end=upper_end,title=title)
    else:
        return render_template("graph.html")


@view.route("/integral",methods=["GET","POST"])
def integral_view():
    if request.method=="POST":
        formula=request.form.get("formula")
        upper_end=request.form.get("upper_end")
        lower_end=request.form.get("lower_end")
        type=request.form.get("type")
        Anser=integral.integral(formula,upper_end,lower_end,type)
        return render_template("integral.html",
        formula=formula,upper_end=upper_end,lower_end=lower_end,type=type,
        anser=Anser[0],anser_upper_end=Anser[1],anser_lower_end=Anser[2],integ=Anser[3])
    else:
        return render_template("integral.html",type="definite_integral_1")


@view.route("/lim",methods=["GET","POST"])
def lim_view():
    if request.method=="POST":
        formula=request.form.get("formula")
        a=request.form.get("a")
        anser=lim.lim(formula,a)
        return render_template("lim.html",formula=formula,a=a,anser_1=anser[0],anser_2=anser[1],lim=anser[2])
    else:
        return render_template("lim.html",a=0)


@view.route("/matrix",methods=["GET","POST"])
def matrix_view():
    if request.method=="POST":
        matrixA=request.form.get("matrix")
        Ar=request.form.get("Ar")
        Ac=request.form.get("Ac")
        type=request.form.get("type")

        Anser=matrix.calculation(matrixA,Ar,Ac,type)

        if Anser[4]=="MATRIX":
            anser=[]
            for i in range(Anser[1]):
                A=str(Anser[0].row(i))
                A=A.replace("Matrix","").replace("**","^").replace("*","").replace("([[","[").replace("]])","]")
                anser.append(A)
        elif Anser[4]=="NUMBER":
            anser=Anser[0]
        return render_template("matrix.html",matrix=matrixA,Ar=Ar,Ac=Ac,type=type,anser_0=anser,anser_3=Anser[3])
    else:
        return render_template("matrix.html",Ar=2,Ac=2,type="A")


@view.route("/matrix_2",methods=["GET","POST"])
def  matrix_2_view():
    if request.method=="POST":
        matrixA=request.form.get("matrixA")
        matrixB=request.form.get("matrixB")
        Ar=request.form.get("Ar")
        Ac=request.form.get("Ac")
        Br=request.form.get("Br")
        Bc=request.form.get("Bc")
        type=request.form.get("type")
        k=request.form.get("k")
        l=request.form.get("l")

        Anser=matrix_2.calculation(matrixA,matrixB,Ar,Ac,Br,Bc,type,k,l)

        anser=[]
        if Anser[0]=="Error":
            anser=[Anser[0]]
        else:
            for i in range(Anser[2]):
                A=str(Anser[0].row(i))
                A=A.replace("Matrix","").replace("**","^").replace("*","").replace("([[","[").replace("]])","]")
                anser.append(A)
        return render_template("matrix_2.html",
        matrixA=matrixA,matrixB=matrixB,Ar=Ar,Ac=Ac,Br=Br,Bc=Bc,type=type,k=k,l=l,
        anser_0=anser,anser_1=Anser[1])
    else:
        return render_template("matrix_2.html",Ar=2,Ac=2,Br=2,Bc=2,type="A",k=2,l=2)


@view.route("/newton_method",methods=["GET","POST"])
def  newton_method_view():
    if request.method=="POST":
        number=request.form.get("number")
        Anser=newton_method.newton_method(number)
        return render_template("newton_method.html",number=number,anser_0=Anser[0],anser_1=Anser[1])
    else:
        return render_template("newton_method.html",anser_0="initial")


@view.route("/prime_factorization",methods=["GET","POST"])
def  prime_factorization_view():
    if request.method=="POST":
        number=request.form.get("number")
        anser=prime_factorization.prime_factorization(number)
        return render_template("prime_factorization.html",number=number,anser=anser)
    else:
        return render_template("prime_factorization.html")


@view.route("/Sieve_of_Eratosthenes",methods=["GET","POST"])
def  Sieve_of_Eratosthenes_view():
    if request.method=="POST":
        number=request.form.get("number")
        Anser=Sieve_of_Eratosthenes.Sieve_of_Eratosthenes(number)
        return render_template("Sieve_of_Eratosthenes.html",number=number,Anser=Anser)
    else:
        return render_template("Sieve_of_Eratosthenes.html")


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
