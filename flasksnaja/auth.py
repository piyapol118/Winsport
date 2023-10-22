from flask import Blueprint

auths = Blueprint('auths', __name__)

@auths.route('/login')
def login():
    return "<h1>login</h1>"

@auths.route('/logout')
def logout():
    return "<h1>logout</h1>"

@auths.route('/signup')
def signup():
    return "<h1>signup</h1>"