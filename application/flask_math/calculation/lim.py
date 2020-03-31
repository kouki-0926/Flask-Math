from sympy import *

x = Symbol('x')

def lim(formula,a):
    try:
        anser = limit(formula, x, a)
    except:
        anser="Error"    
    return anser
