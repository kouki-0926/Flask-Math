from sympy import *

x = Symbol('x')

def equation(formula):
    try:
        anser= solve(formula, dict = True)
    except:
        anser=["Error"]
    return anser
