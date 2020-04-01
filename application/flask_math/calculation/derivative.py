from sympy import *
from flask import flash

x = Symbol('x')
y = Symbol('y')

def derivative(formula,a):
    try:
        if a=="x":
            A = diff(formula,x)
        elif a=="y":
            A = diff(formula,y)
        elif a=="xx":
            f = diff(formula,x)
            A = diff(f,x)
        elif a=="xy":
            f = diff(formula,x)
            A = diff(f,y)
        elif a=="yx":
            f = diff(formula,y)
            A = diff(f,x)
        elif a=="yy":
            f = diff(formula,y)
            A = diff(f,y)

        formula=str(formula)
        formula="f = "+formula.replace("**","A").replace("*","").replace("A","^")
        A=str(A)
        A=" = "+A.replace("**","A").replace("*","").replace("A","^")

        anser=[formula,"f",a,A]
    except:
        anser=["Error","","",""]
        flash("エラー：もう一度入力してください")
    return anser
