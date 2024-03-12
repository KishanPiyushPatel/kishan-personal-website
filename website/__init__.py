from flask import Flask


def create_app():
    app = Flask(__name__)
    # secure key for production
    app.config['SECRET_Key'] = 'bfjhfjhfvbjh jhdfkerg'
    
    from .views import views
    app.register_blueprint(views, url_prefix='/')

    return app

    