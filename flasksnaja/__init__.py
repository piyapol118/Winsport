from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "alo everyone"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"

    from .models import User, Note

    create_database(app)

    from .routez import routes
    app.register_blueprint(routes)
    
    return app

def create_database(app):
    if not path('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
