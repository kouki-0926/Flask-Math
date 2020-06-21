import matplotlib.pyplot as plt
import math
import numpy as np
from  sympy import *

def graph(formula,lower_end,upper_end,title):
    #x=np.linspace(int(lower_end),int(upper_end),100)
    #f=np.vectorize(formula)
    x = np.linspace(-np.pi, np.pi, 201)
    plt.plot(x, np.sin(x))
    #x=Symbol("x")
    #f=sympify(formula)
    #f=np.sin(x)
    #f=formula
    # plt.plot(x,f)
    # plt.suptitle(str(title),fontname="MS Gothic",fontsize=18)
    # plt.legend(str(f))
    plt.show()
