from flask import Blueprint, render_template

routes = Blueprint("routes", __name__)

@routes.route("/")
def home():
    return "home_page"

@routes.route("/map")
def maps():
    return render_template("routemap.html")

@routes.route("/sec")
def sec():
    return render_template("second_page.html")


@routes.route("/third")
def third():
    return render_template("third.html")


@routes.route("/about")
def about():
    return render_template("about_page.html")
