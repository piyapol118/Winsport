from flask import Blueprint, render_template

routes = Blueprint("routes", __name__)

@routes.route("/")
def home():
    return "home_page"

@routes.route("/map")
def maps():
    return render_template("routemap.html")