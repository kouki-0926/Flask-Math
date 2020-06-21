from sympy import *
from sympy.plotting import plot
from flask import flash

def graph(formula,lower_end,upper_end):
    try:
        x = Symbol('x')
        formula=sympify(formula)
        lower_end=sympify(lower_end)
        upper_end=sympify(upper_end)
        plot(formula,(x,lower_end,upper_end),legend=True)
    except:
        flash("エラー：もう一度入力してください")
