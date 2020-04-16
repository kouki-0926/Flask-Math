from sympy import *
from flask import flash

x = Symbol('x')

def equation(formula):
    try:
        Anser=solve(formula, dict = True)
    except:
        Anser=["Error"]
        flash("エラー：もう一度入力してください")
    return Anser
