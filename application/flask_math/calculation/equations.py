from sympy import *
from flask import flash

def equations(formula):
    try:
        anser=solve(formula)
    except:
        anser="Error"
        flash("エラー：もう一度入力してください")
    return anser
