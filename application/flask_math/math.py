from sympy import *

def integral(formula):
    try:
        anser=integrate(formula)
    except:
        anser="被積分関数を入力してください"
    return anser


def derivative(formula):
    try:
        anser=diff(formula)
    except:
        anser="被積分関数を入力してください"
    return anser
