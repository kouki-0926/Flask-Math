from sympy import *
from flask import flash
from flask_math.calculation.generate.MATRIX import MATRIX

def calculation(matrixA,matrixB,Ar,Ac,Br,Bc,type,k,l):
    try:
        Ar,Ac,Br,Bc,k,l=[int(Ar),int(Ac),int(Br),int(Bc),int(k),int(l)]

        A=MATRIX(matrixA,Ar,Ac)
        B=MATRIX(matrixB,Br,Bc)

        if type=="A":
            anser=A
            type="A = "
            anser_r=Ar
            anser_c=Ac

        elif type=="B":
            anser=B
            type="B = "
            anser_r=Br
            anser_c=Bc

        elif type=="kA+lB":
            anser=k*A+l*B
            type=str(k)+"A+"+str(l)+"B = "
            anser_r=Ar
            anser_c=Ac

        elif type=="AB":
            anser=A*B
            type="AB = "
            anser_r=Ar
            anser_c=Bc

        elif type=="BA":
            anser=B*A
            type="BA = "
            anser_r=Br
            anser_c=Ac
    except:
        anser="Error"
        type=""
        anser_r=""
        anser_c=""
        flash("エラー：もう一度入力してください")

    Anser=[anser,type,anser_r,anser_c]

    return Anser
