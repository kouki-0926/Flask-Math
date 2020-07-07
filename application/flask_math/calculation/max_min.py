from sympy import *
from flask import flash

x,y=symbols('x y')

def max_min(formula):
    try:
        f=sympify(formula)
        f_x=diff(f,x)
        f_xx=diff(f,x,2)
        A=solve(f_x, dict = True)

        Max_Anser=[]
        Min_Anser=[]
        for i in range(len(A)):
            a=A[i]
            for B in a.items():
                b=f_xx.subs(x,B[1])
                c=f.subs(x,B[1])
                if b>=0:
                    anser="極小値　f("+str(B[1])+") = "+str(c)
                    Min_Anser.append(anser)
                else:
                    anser="極大値　f("+str(B[1])+") = "+str(c)
                    Max_Anser.append(anser)
        Anser=Max_Anser+[""]+Min_Anser
    except:
        Anser=["Error"]
        flash("エラー：もう一度入力してください")
    return Anser
