from flask import make_response
try:
    from flask_math.calculation.common.STR import LATEX
except:
    from common.STR import LATEX
from matplotlib.backends.backend_agg import FigureCanvasAgg
import matplotlib.pyplot as plt
from control.matlab import *
from sympy import *
import numpy as np
from io import BytesIO

s, t = symbols('s, t')
w = symbols('w', real=True)

lower_end_x = -2
upper_end_x = 5
num = 300


def sysio(formula, formula_2):
    output = simplify(formula)*simplify(formula_2)
    anser = inverse_laplace_transform(output, s, t)

    # データ作成
    T = np.linspace(lower_end_x, upper_end_x, num)
    Y = np.array([anser.subs(t, T[i]) for i in range(len(T))])

    fig = plt.figure(figsize=(7, 4))
    plt.plot(T, Y)
    plt.title("$y(t)="+LATEX(anser)+"("+str(lower_end_x)+"<t<"+str(upper_end_x)+")$")

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
