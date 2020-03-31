from sympy import *
from flask import flash

x = Symbol('x')

def lim(formula,a):
    try:
        a=float(a)
        A=str(limit(formula, x, a))

        a=str(a)
        formula=str(formula)
        anser=["lim  "+formula+ " = "+A,"x→"+a]
    except:
        anser=["Error",""]
        flash("エラー:もう一度関数を入力してください")
    return anser
