from sympy import *
from flask import flash
from flask_math.calculation.common.STR import STR

x = Symbol('x')

def integral(formula,upper_end,lower_end,type):
    try:
        g=integrate(formula)
        A=g.subs(x,upper_end)-g.subs(x,lower_end)

        if type=="definite_integral_1":
            anser=STR(formula)+"dx = "+str(A)
        elif type=="definite_integral_2":
            anser=STR(formula)+"dx = "+str(A.evalf())
        elif type=="indefinite_integral":
            anser=STR(formula)+"dx = "+STR(g)+"+c"
            upper_end=""
            lower_end=""

        Anser=[anser,upper_end,lower_end,"∫"]
    except:
        Anser=["Error","","",""]
        flash("エラー:もう一度入力してください")
    return Anser
