from sympy import *
from flask import flash

x = Symbol('x')
y = Symbol('y')

def derivative(formula,type):
    try:
        if type=="x":
            A = diff(formula,x)
        elif type=="y":
            A = diff(formula,y)
        elif type=="xx":
            f = diff(formula,x)
            A = diff(f,x)
        elif type=="xy":
            f = diff(formula,x)
            A = diff(f,y)
        elif type=="yx":
            f = diff(formula,y)
            A = diff(f,x)
        elif type=="yy":
            f = diff(formula,y)
            A = diff(f,y)

        formula=str(formula)
        A=str(A)
        formula="f = "+formula.replace("**","A").replace("*","").replace("A","^")
        A=" = "+A.replace("**","A").replace("*","").replace("A","^")

        anser=[formula,"f",type,A]
    except:
        anser=["Error","","",""]
        flash("エラー：もう一度入力してください")
    return anser
