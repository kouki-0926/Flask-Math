from flask import flash

def newton_method(number):
    try:
        number=float(number)
        if number>0:
            ε=10**-10

            num_old=number
            num_new=number/2
            while abs(1-num_old/num_new)>ε:
                num_old=num_new
                num_new=(num_old+number/num_old)/2

            anser=" = "+str(num_new)
            Anser=[number,anser]
        else:
            Anser=["Error",""]
            flash("エラー：正の数を入力してください")
    except:
        Anser=["Error",""]
        flash("エラー：もう一度入力してください")
    return Anser
