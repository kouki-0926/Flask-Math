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
            A = diff(formula,x,x)
        elif type=="xy":
            A = diff(formula,x,y)
        elif type=="yx":
            A = diff(formula,y,x)
        elif type=="yy":
            A = diff(formula,y,y)

        formula=str(formula)
        A=str(A)
        formula="f = "+formula.replace("**","A").replace("*","").replace("A","^")
        A=" = "+A.replace("**","A").replace("*","").replace("A","^")

        anser=[formula,"f",type,A]
    except:
        anser=["Error","","",""]
        flash("エラー：もう一度入力してください")
    return anser
