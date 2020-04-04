from sympy import *

def calculation(matrixA,Ar,Ac,c):
    try:
        matrixA_list=list(matrixA)
        List=[]
        for k in range(Ar):
            List.append([])

        for j in range(0,Ar,1):
            for i in range(j*(3*Ac+1),(j+1)*(3*Ac+1)-3,3):
                if matrixA_list[i]==" ":
                    m=int(matrixA_list[i+1])
                else:
                    m=-int(matrixA_list[i+1])
                List[j].append(m)

        A=Matrix(List)

        Anser=[]
        if c==0:
            anser=A
            anser_r=Ar
            anser_c=Ac
            type="A = "
            d=0

        elif c==1:
            A=A.diagonalize()
            A=list(A)
            P=A[0]
            A=A[1]
            for i in range(0,Ac,1):
                A[i,i]="("+str(A[i,i])+")^n"
            anser=P*A*P.inv()
            anser_r=Ar
            anser_c=Ac
            type="A^n = "
            d=0

        elif c==2:
            anser=A.transpose()
            anser_r=Ac
            anser_c=Ar
            type="A^t = "
            d=0

        elif c==3:
            anser=A.inv()
            anser_r=Ar
            anser_c=Ac
            type="A^-1 = "
            d=0

        elif c==4:
            anser=A.adjugate()
            anser_r=Ar
            anser_c=Ac
            type="A~ = "
            d=0

        elif c==5:
            anser=A.det()
            anser_r=Ar
            anser_c=Ac
            type="det(A) = "
            d=1

        elif c==6:
            anser=A.rank()
            anser_r=Ar
            anser_c=Ac
            type="rank(A) = "
            d=1

        elif c==7:
            anser=A.trace()
            anser_r=Ar
            anser_c=Ac
            type="tr(A) = "
            d=1

        elif c==8:
            A=A.eigenvals()
            anser=list(A)
            anser_r=Ar
            anser_c=Ac
            type="λ = "
            d=1

        elif c==9:
            A=A.diagonalize()
            A=list(A)
            anser=A[0]
            anser_r=Ar
            anser_c=Ac
            type="P = "
            d=0

        elif c==10:
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

    Anser=[anser,anser_r,anser_c,type,d]

    return Anser
