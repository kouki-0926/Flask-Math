from sympy import *
from sympy.plotting import plot,plot3d
from flask import flash

def graph(Formula,Lower_end,Upper_end,dimension):
    try:
        x,y=symbols('x y')
        Formula=sympify(Formula)
        lower_end_x=sympify(Lower_end[0])
        upper_end_x=sympify(Upper_end[0])
        if dimension=="3D":
            lower_end_y=sympify(Lower_end[1])
            upper_end_y=sympify(Upper_end[1])
            plot3d(Formula[0],Formula[1],(x, lower_end_x, upper_end_x),(y, lower_end_y, upper_end_y),legend=True)
        elif dimension=="2D":
            plot(Formula[0],Formula[1],(x,lower_end_x,upper_end_x),legend=True)
    except:
        flash("エラー：もう一度入力してください")
