import numpy as np
from flask import flash, make_response
from matplotlib.backends.backend_agg import FigureCanvasAgg
import matplotlib.pyplot as plt
from io import BytesIO
from sympy import *


def bode(formula, lower_end, upper_end):
    s = symbols('s')
    formula = sympify(formula)

    # データ作成
    w, g, φ = [], [], []
    for i in range(int(lower_end)*10, int(upper_end)*10, 1):
        c = 10**(0.1*i)
        a = 20*log(Abs(formula.subs(s, I*c)), 10)
        b = arg(formula.subs(s, I*c))*180/pi
        if(a != zoo):
            w.append(c)
            g.append(a)
            φ.append(b)

    fig = plt.figure(figsize=(7, 4))
    ax1 = fig.add_subplot(2, 1, 1)
    ax2 = fig.add_subplot(2, 1, 2)

    ax1.plot(w, g)
    ax1.set_xscale("log")
    ax1.set_title("G(s)="+str(formula))

    ax2.plot(w, φ)
    ax2.set_xscale("log")

    # canvasにプロットした画像を出力
    canvas = FigureCanvasAgg(fig)
    png_output = BytesIO()
    canvas.print_png(png_output)
    data = png_output.getvalue()
    # HTML側に渡すレスポンスを生成する
    response = make_response(data)
    response.headers['Content-Type'] = 'image/png'
    response.headers['Content-Length'] = len(data)
    return response
