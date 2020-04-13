from sympy import *
from flask import flash
from flask_math.calculation.generate.STR import STR

x = Symbol('x')

def taylor(formula,dimension,center):
    try:
        f=sympify(formula)
        center=float(center)

        A=f.subs(x,center)
        for number in range(1,int(dimension)+1,1):
            f=diff(f)
            D=f.subs(x,center)/factorial(number)

            A=D*(x-center)**number+A

        anser=STR(formula)+"≒"+STR(A)
    except:
        anser="Error"
        flash("エラー：もう一度入力してください")
    return anser
