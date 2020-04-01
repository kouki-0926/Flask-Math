from sympy import *
from flask import flash

x = Symbol('x')

def integral(formula,upper_end,lower_end,type):
    try:
        g=integrate(formula)
        A=g.subs(x,upper_end)-g.subs(x,lower_end)

        if type=="0":
            anser="∫["+str(lower_end)+"→"+str(upper_end)+"]"+formula+" = "+str(A)
        elif type=="1":
            anser="∫["+str(lower_end)+"→"+str(upper_end)+"]"+formula+" = "+str(A.evalf())
        elif type=="2":
            g=str(g)
            anser="∫"+formula+" = "+g.replace("**","A").replace("*","").replace("A","^")+"+C"
        return anser
    except:
        anser="Error"
        flash("エラー:もう一度入力してください")
        return anser
