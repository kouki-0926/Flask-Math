from sympy import *
from flask import flash

def factorization(formula):
    try:
        A=factor(formula)

        A=str(A)
        formula=str(formula)
        A=A.replace("**","C").replace("*","").replace("C","^")
        formula=formula.replace("**","C").replace("*","").replace("C","^")

        anser=formula+" = "+A
    except:
        anser="Error"
        flash("エラー：もう一度入力してください")
    return anser
