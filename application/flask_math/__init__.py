from flask import Flask

def create_app():
    app=Flask(__name__)
    app.config.from_object("flask_math.config")

    from flask_math.views import view
    app.register_blueprint(view)

    return app
