from sympy import *
from flask import flash

x = Symbol('x')

def integral(formula,upper_end,lower_end,type):
    try:
        g=integrate(formula)
        A=g.subs(x,upper_end)-g.subs(x,lower_end)

        if type=="0":
            anser=A
        elif type=="1":
            anser=A.evalf()
        elif type=="2":
            g=str(g)
            anser=g.replace("**","A").replace("*","").replace("A","^")
        return anser
    except:
        anser="Error"
        flash("エラー:もう一度入力してください")
        return anser
