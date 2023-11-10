from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify, session
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

routes = Blueprint("routes", __name__)

button_state = 0

@routes.route("/")
def home():
    return render_template("index.html", user=None)

@routes.route("/map")
def maps():
    return render_template("routemap.html", user=current_user)

@routes.route("/sec")
def sec():
    return render_template("second_page.html", user=current_user)

@routes.route("/third")
def third():
    return render_template("third.html", user=current_user)

@routes.route("/about")
def about():
    return render_template("about_page.html", user=current_user)

@routes.route("/rate")
def rate():
    return render_template("rate_of_price.html", user=current_user)

@routes.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('/login')

<<<<<<< Updated upstream
@routes.route("/addfav") #page display your fav
def another_page():
    email = session.get("email")
    
    user = User.query.filter_by(email=email).first()
    if user:
        button_state = user.button_state
        first_name = user.first_name
        if button_state == 1:
            image = "../static/public/สถาบันเทคโนโลยีพระจอมเกล้าเจ้าคุณทหารลาดกระบัง001.jpg"
            message = None
        else:
            image = None
            message = "Not Have Favorite"
    else:
        flash("ไม่พบบัญชี", category="error")
        return redirect("/register")
    return render_template("favorite.html", message=message, image=image, button_state=image, email=email, first_name=first_name, user=current_user)

@routes.route("/pro", methods=['GET']) #demo profile but have fav button
@login_required 
def pro():
    
    email = session.get("email")
    
    user = User.query.filter_by(email=email).first()
    if user:
        button_state = user.button_state
        first_name = user.first_name
        if button_state == 1:
            image_path = "../static/public/สถาบันเทคโนโลยีพระจอมเกล้าเจ้าคุณทหารลาดกระบัง001.jpg"
        else:
            image_path = "../static/public/morter-removebg-preview.png"
        return render_template("profile.html", first_name=first_name ,email=email, user=current_user, button_state=image_path, image_path=image_path)
    else:
        flash("ไม่พบบัญชี", category="error")
        return redirect("/register")
    
@routes.route("/toggle", methods=['POST']) #the buttun that can change data
@login_required
def toggle():
    email = session.get("email")
    
    # Retrieve user from the database
    user = User.query.filter_by(email=email).first()
    
    # Toggle the button state between 0 and 1
    if user:
        user.button_state = 1 - user.button_state
        db.session.commit()

    button_state = user.button_state
    
    if button_state == 1:
        image_url = "../static/public/สถาบันเทคโนโลยีพระจอมเกล้าเจ้าคุณทหารลาดกระบัง001.jpg"
    else:
        image_url = "../static/public/morter-removebg-preview.png"
    return jsonify({"image_url": image_url, "button_state": button_state})
=======

@routes.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('/login')
>>>>>>> Stashed changes

@routes.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('ล็อกอินสำเร็จ!', category="success")
                login_user(user, remember=True)
                session["email"] = email
                return redirect('/sec')
            else:
                flash('รหัสผ่านไม่ถูกต้อง กรุณาลองอีกครั้ง', category="error")
        else:
            flash("ชื่อของคุณไม่มีในระบบ", category='error')

    return render_template("Login_page.html", user=current_user)

@routes.route("/register", methods=["GET", "POST"])
def regist():
    if request.method == "POST":
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        
        if user:
            flash('อีเมลดังกล่าวถูกใช้งานแล้ว', category='error')
        elif len(first_name) < 3:
            flash("ชื่อผู้ใช้ต้องมีความยาวไม่ต่ำกว่า 3 ตัวอักษร", category='error')
        elif len(email) < 4 or "@" not in email:
            flash("อีเมลของคุณไม่ถูกต้อง", category="error")
        elif password1 != password2:
            flash("รหัสผ่านไม่ตรงกัน", category='error')
        elif len(password1) < 7:
            flash("รหัสผ่านต้องมีความยาวไม่ต่ำกว่า 7 ตัวอักษร", category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash("สร้างบัญชีผู้ใช้สำเร็จ", category='success')
            return redirect('/')

            # add user to database 
    return render_template("register_page.html", user=current_user)
