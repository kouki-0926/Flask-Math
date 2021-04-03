import numpy as np
from flask import flash, make_response
from matplotlib.backends.backend_agg import FigureCanvasAgg
import matplotlib.pyplot as plt
from io import BytesIO
from sympy import *
from math import degrees
import numpy as np


def bode(formula, lower_end, upper_end, width):
    s = symbols('s')
    w_pi_flag = 0
    formula = sympify(formula)

    # データ作成
    w, g, φ = [], [], []
    for i in range(int(lower_end)*width, int(upper_end)*width, 1):
        c = 10**(i/width)
        a = 20*log(Abs(formula.subs(s, I*c)), 10)
        b = degrees(arg(formula.subs(s, I*c)))
        if(b >= 0):
            b -= 360
        if((-185 <= b) & (b <= -175)):
            w_pi = c
            w_pi_flag = 1
        if(a != zoo):
            w.append(c)
            g.append(a)
            φ.append(b)

    if(w_pi_flag):
        b_2_list = [[], []]
        for j in range(int((w_pi-1)*100), int((w_pi+1)*100), 1):
            c_2 = j/100
            b_2 = degrees(arg(formula.subs(s, I*c_2)))
            if(b_2 >= 0):
                b_2 -= 360
            b_2_list[0].append(abs(b_2+180))
            b_2_list[1].append(c_2)
            w_pi_2 = b_2_list[1][np.argmin(b_2_list[0])]
            Gm = float(-20*log(Abs(formula.subs(s, I*w_pi_2)), 10))

    fig = plt.figure()
    ax1 = fig.add_subplot(2, 1, 1)
    ax2 = fig.add_subplot(2, 1, 2)

    ax1.plot(w, g)
    ax1.axhline(y=0, xmin=int(lower_end), xmax=int(upper_end), color="black")
    ax1.set_xscale("log")
    if(w_pi_flag):
        ax1.set_title("G(s)="+str(formula)+", ωπ="+str(w_pi_2)+"rad/s, Gm="+str(round(Gm, 2))+"dB")
    else:
        ax1.set_title("G(s)="+str(formula))

    ax2.plot(w, φ)
    ax2.axhline(y=-180, xmin=int(lower_end), xmax=int(upper_end), color="black")
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
