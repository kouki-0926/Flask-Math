from sympy import *
from flask import flash

def Expand(formula):
    try:
        A=expand(formula)

        A=str(A)
        formula=str(formula)
        A=A.replace("**","C").replace("*","").replace("C","^")
        formula=formula.replace("**","C").replace("*","").replace("C","^")

        anser=formula+" = "+A
    except:
        anser="Error"
        flash("エラー：もう一度入力してください")
    return anser
