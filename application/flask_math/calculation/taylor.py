from sympy import*

x = Symbol('x')

def taylor(formula,dimension,center,type,d):
    try:
        f=integrate(formula)
        f=diff(f)

        A=f.subs(x,center)
        for number in range(1,dimension+1,1):
            f=diff(f)
            D=f.subs(x,center)/factorial(number)

            if type==1:
                D=D
            else:
                d=10**(-d)
                if abs(D)<d:
                    D=0
                else:
                    D=D

            A=D*(x-center)**number+A

        A=str(A)
        anser=str(formula)+"≒"+str(A.replace("**","B").replace("*","").replace("B","^"))
        anser_2=str(formula)+"≒"+str(A)
        print("------------------------------------------------------------------------------------------------------------------------")
        print(anser)
        print("")
        print(anser_2)
        print("")
    except:
        anser="Error"
        print("Error")
    return anser
