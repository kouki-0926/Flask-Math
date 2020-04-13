from sympy import *
from flask import flash
from flask_math.calculation.generate.MATRIX import MATRIX

def calculation(matrixA,Ar,Ac,type):
    try:
        Ar,Ac=[int(Ar),int(Ac)]
        A=MATRIX(matrixA,Ar,Ac)

        if type=="A":
            anser=A
            anser_r=Ar
            anser_c=Ac
            type="A = "
            d=0

        elif type=="A^n":
            A=A.diagonalize()
            A=list(A)
            P=A[0]
            D=A[1]
            for i in range(0,Ac,1):
                D[i,i]="("+str(D[i,i])+")^n"
            anser=P*D*P.inv()
            anser_r=Ar
            anser_c=Ac
            type="A^n = "
            d=0

        elif type=="A^t":
            anser=A.transpose()
            anser_r=Ac
            anser_c=Ar
            type="A^t = "
            d=0

        elif type=="A^-1":
            anser=A.inv()
            anser_r=Ar
            anser_c=Ac
            type="A^-1 = "
            d=0

        elif type=="A~":
            anser=A.adjugate()
            anser_r=Ar
            anser_c=Ac
            type="A~ = "
            d=0

        elif type=="det(A)":
            anser=A.det()
            anser_r=Ar
            anser_c=Ac
            type="det(A) = "
            d=1

        elif type=="rank(A)":
            anser=A.rank()
            anser_r=Ar
            anser_c=Ac
            type="rank(A) = "
            d=1

        elif type=="tr(A)":
            anser=A.trace()
            anser_r=Ar
            anser_c=Ac
            type="tr(A) = "
            d=1

        elif type=="λ":
            A=A.eigenvals()
            anser=list(A)
            anser_r=Ar
            anser_c=Ac
            type="λ = "
            d=1

        elif type=="P":
            A=A.diagonalize()
            A=list(A)
            anser=A[0]
            anser_r=Ar
            anser_c=Ac
            type="P = "
            d=0

        elif type=="P^-1AP":
            A=A.diagonalize()
            A=list(A)
            anser=A[1]
            anser_r=Ar
            anser_c=Ac
            type="P^-1AP = "
            d=0
    except:
        anser="Error"
        anser_r=""
        anser_c=""
        type=""
        d=1
        flash("エラー：もう一度入力してください")

    Anser=[anser,anser_r,anser_c,type,d]

    return Anser
