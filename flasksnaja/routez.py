from flask import Blueprint, render_template, request, flash

routes = Blueprint("routes", __name__)

@routes.route("/")
def home():
    return render_template("index.html")

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

@routes.route("/login", methods=["GET", "POST"])
def login():
    return render_template("Login_page.html", boolean=True)

@routes.route("/register", methods=["GET", "POST"])
def regist():
    if request.method == "POST":
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(firstName) < 3:
            flash("ชื่อผู้ใช้ต้องมีความยาวไม่ต่ำกว่า 3 ตัวอักษร", category='error')
        elif len(email) < 4 or "@" not in email:
            flash("อีเมลของคุณไม่ถูกต้อง", category="error")
        elif password1 != password2:
            flash("รหัสผ่านไม่ตรงกัน", category='error')
        elif len(password1) < 7:
            flash("รหัสผ่านต้องมีความยาวไม่ต่ำกว่า 7 ตัวอักษร", category='error')
        else:
            flash("สร้างบัญชีผู้ใช้สำเร็จ", category='success')
        
            # add user to database 
    return render_template("register_page.html")
