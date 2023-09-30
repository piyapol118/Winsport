from flask import Flask

def create_app():
    app = Flask(__name__)

    from .site import web
    app.register_blueprint(web, url_prefix="/")

    return app