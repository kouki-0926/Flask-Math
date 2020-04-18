from flask_math.calculation.common.NEWTON_METHOD import NEWTON_METHOD
from flask import flash

def Sieve_of_Eratosthenes(N):
    try:
        N=int(N)
        List=list(range(2,N))
        prime_List=[]

        MIN=0
        while MIN<NEWTON_METHOD(N):
            MIN=min(List)
            prime_List.append(MIN)
            List=[i for i in List if i % MIN != 0]

        prime_List=prime_List+List


        prime_List_List=[str(N)+"以下の素数"]
        n=15
        for i in range(len(prime_List)//n+1):
            prime_List_List.append(prime_List[n*i:n*i+n])
    except:
        prime_List_List=["Error"]
        flash("エラー：もう一度入力してください")
    return prime_List_List
