from sympy import *

def equations(formula):
    try:
        anser=solve(formula)
    except:
        anser="Error"    
    return anser
