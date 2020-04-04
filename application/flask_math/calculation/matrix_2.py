from sympy import *

def calculation(matrixA,matrixB,Ar,Ac,Br,Bc,e,k,l):
    try:
        matrixA_list=list(matrixA)
        List_A=[]
        for p in range(Ar):
            List_A.append([])
            
        matrixB_list=list(matrixB)
        List_B=[]
        for q in range(Br):
            List_B.append([])

        for j in range(0,Ar,1):
            for i in range(j*(3*Ac+1),(j+1)*(3*Ac+1)-3,3):
                if matrixA_list[i]==" ":
                    m=int(matrixA_list[i+1])
                else:
                    m=-int(matrixA_list[i+1])
                List_A[j].append(m)

        A=Matrix(List_A)

        for j in range(0,Br,1):
            for i in range(j*(3*Bc+1),(j+1)*(3*Bc+1)-3,3):
                if matrixB_list[i]==" ":
                    m=int(matrixB_list[i+1])
                else:
                    m=-int(matrixB_list[i+1])
                List_B[j].append(m)

        B=Matrix(List_B)

        if e==0:
            anser=A
            type="A = "
            anser_r=Ar
            anser_c=Ac

        elif e==1:
            anser=B
            type="B = "
            anser_r=Br
            anser_c=Bc

        elif e==2:
            anser=k*A+l*B
            type=str(k)+"A+"+str(l)+"B = "
            anser_r=Ar
            anser_c=Ac

        elif e==3:
            anser=A*B
            type="AB = "
            anser_r=Ar
            anser_c=Bc

        elif e==4:
            anser=B*A
            type="BA = "
            anser_r=Br
            anser_c=Ac
    except:
        anser=""
        type="Error"
        anser_r=""
        anser_c=""

    Anser=[anser,type,anser_r,anser_c]

    return Anser
