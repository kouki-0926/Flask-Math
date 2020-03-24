from sympy import *
from flask import flash

def integral(formula):
    try:
        A=str(integrate(formula))

        f=formula.replace("**","B").replace("*","").replace("B","^")
        A=A.replace("**","B").replace("*","").replace("B","^")
        anser="∫"+f+"dx = "+A+"+C"
    except:
        anser="Error"
        flash("もう一度被積分関数を入力してください")
    return anser


def derivative(formula):
    try:
        A=str(diff(formula))

        f=formula.replace("**","B").replace("*","").replace("B","^")
        A=A.replace("**","B").replace("*","").replace("B","^")
        anser="d/dx("+f+") = "+A
    except:
        anser="Error"
        flash("エラー　もう一度関数を入力してください")
    return anser


def taylor(formula,a,b):
    try:
        x=symbols("x")
        a=int(a)
        b=float(b)
        f=integrate(formula)
        f=diff(f)

        A=f.subs(x,b)
        for number in range(1,int(a)+1,1):
            f=diff(f)
            B=f.subs(x,b)/factorial(number)
            A=B*(x-b)**number+A

        A=str(A)
        anser=str(formula)+"≒"+str(A.replace("**","B").replace("*","").replace("B","^"))
    except:
        anser="Error"
        flash("エラー　もう一度入力してください")
    return anser
