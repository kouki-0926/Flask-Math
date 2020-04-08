from sympy import*
from flask import flash

x = Symbol('x')

def taylor(formula,dimension,center):
    try:
        f=sympify(formula)
        center=float(center)

        A=f.subs(x,center)
        for number in range(1,int(dimension)+1,1):
            f=diff(f)
            D=f.subs(x,center)/factorial(number)

            A=D*(x-center)**number+A

        A=str(A)
        anser=str(formula)+"≒"+str(A.replace("**","B").replace("*","").replace("B","^"))
    except:
        anser="Error"
        flash("エラー：もう一度入力してください")
    return anser
