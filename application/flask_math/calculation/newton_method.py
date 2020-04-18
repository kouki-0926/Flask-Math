from flask_math.calculation.common.NEWTON_METHOD import NEWTON_METHOD
from flask import flash

def newton_method(number):
    try:
        anser="="+str(NEWTON_METHOD(number))
        Anser=[number,anser]
    except:
        Anser=["Error",""]
        flash("エラー：もう一度入力してください")
    return Anser
