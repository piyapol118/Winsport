from os import path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"
UPLOAD_FOLDER = 'flasksnaja/static/public/uploads'


app = Flask(__name__)
app.config['SECRET_KEY'] = "alo everyone"
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
db.init_app(app)

from .routez import routes
app.register_blueprint(routes)

from .models import User

with app.app_context():
    db.create_all()

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))
