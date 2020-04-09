from sympy import *
from flask import flash

x = Symbol('x')

def integral(formula,upper_end,lower_end,type):
    try:
        g=integrate(formula)
        A=g.subs(x,upper_end)-g.subs(x,lower_end)

        if type=="definite_integral":
            anser=str(formula)+"dx = "+str(A)
        elif type=="indefinite_integral_1":
            anser=str(formula)+"dx = "+str(A.evalf())
        elif type=="indefinite_integral_2":
            g=str(g)
            anser=str(formula)+"dx = "+g.replace("**","A").replace("*","").replace("A","^")+"+C"
            upper_end=""
            lower_end=""

        Anser=[anser,upper_end,lower_end,"∫"]
    except:
        Anser=["Error","","",""]
        flash("エラー:もう一度入力してください")
    return Anser
