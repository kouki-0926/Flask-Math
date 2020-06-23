from sympy import *
from flask import flash

x = Symbol('x')

def equation(formula):
    try:
        A=solve(formula, dict = True)

        Anser=[]
        for i in range(len(A)):
            a=A[i]
            for B in a.items():
                anser=str(B[0])+"="+str(B[1])
                Anser.append(anser)
    except:
        Anser=["Error"]
        flash("エラー：もう一度入力してください")
    return Anser
