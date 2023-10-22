from flask import Flask

def create_app():
    app = Flask(__name__)

    from .routez import routes
    from .auth import auths
    
    app.register_blueprint(auths)
    app.register_blueprint(routes)
    
    return app