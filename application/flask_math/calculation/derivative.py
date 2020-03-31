from sympy import *

x = Symbol('x')
y = Symbol('y')

def derivative(formula,a):
    try:
        if a=="x":
            A = diff(formula,x)
        elif a=="y":
            A = diff(formula,y)
        elif a=="xx":
            f = diff(formula,x)
            A = diff(f,x)
        elif a=="xy":
            f = diff(formula,x)
            A = diff(f,y)
        elif a=="yx":
            f = diff(formula,y)
            A = diff(f,x)
        elif a=="yy":
            f = diff(formula,y)
            A = diff(f,y)

        A=str(A)
        anser=A.replace("**","A").replace("*","").replace("A","^")
    except:
        anser="Error"
    return anser
