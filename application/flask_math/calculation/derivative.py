from sympy import *
from flask import flash

x = Symbol('x')
y = Symbol('y')

def derivative(formula,a):
    try:
        if a=="x":
            A = diff(formula,x)
            b = "d"
            c = "dx"
        elif a=="y":
            A = diff(formula,y)
            b = "d"
            c = "dy"
        elif a=="xx":
            f = diff(formula,x)
            A = diff(f,x)
            b = "∂^2"
            c = "∂x^2"
        elif a=="xy":
            f = diff(formula,x)
            A = diff(f,y)
            b = "∂^2"
            c = "∂y∂x"
        elif a=="yx":
            f = diff(formula,y)
            A = diff(f,x)
            b = "∂^2"
            c = "∂x∂y"
        elif a=="yy":
            f = diff(formula,y)
            A = diff(f,y)
            b = "∂^2"
            c = "∂y^2"

        formula=str(formula)
        formula=formula.replace("**","A").replace("*","").replace("A","^")
        A=str(A)
        A=A.replace("**","A").replace("*","").replace("A","^")
        anser=[b,c,"------    {"+formula+"} = "+A]
    except:
        anser=["","","Error"]
        flash("エラー：もう一度入力してください")
    return anser
