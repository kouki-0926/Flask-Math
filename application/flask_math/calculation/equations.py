from sympy import *
from flask import flash
from flask_math.calculation.generate.STR import STR

def equations(formula):
    try:
        A=solve(formula)

        Anser=[]
        for B in A.items():
            anser=STR(B[0])+" = "+STR(B[1])
            Anser.append(anser)
    except:
        Anser=["Error"]
        flash("エラー：もう一度入力してください")
    return Anser
