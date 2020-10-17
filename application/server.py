import sys
sys.dont_write_bytecode=True

from flask import Flask
from flask_math.views import Math

app=Flask(__name__)
app.config.from_object("config")
app.register_blueprint(Math,url_prefix="/flask_math")

if __name__=="__main__":
    app.run()
    # app.run(host="0.0.0.0",port=5000)
