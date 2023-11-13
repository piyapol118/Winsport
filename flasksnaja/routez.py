from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify, session
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
import os
from flask_login import login_user, login_required, logout_user, current_user
from flasksnaja import app

routes = Blueprint("routes", __name__)
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
button_state = 0
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@routes.route("/")
def home():
    return render_template("index.html", user=current_user)

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


@routes.route("/pro_test", methods=['GET', 'POST']) #demo profile but have fav button
@login_required 
def pro_test():
    email = session.get("email")
    
    user = User.query.filter_by(email=email).first()
    if user:
        first_name = user.first_name
        return render_template("profile_page.html", first_name=first_name ,email=email, user=current_user)
    else:
        flash("ไม่พบบัญชี", category="error")
        return redirect("/register")

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
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash("สร้างบัญชีผู้ใช้สำเร็จ", category='success')
            return redirect('/')

            # add user to database 
    return render_template("register_page.html", user=current_user)

@routes.route('/upload-endpoint', methods=['POST'])
@login_required
def upload_file():
    email = session.get("email")
    if 'image' not in request.files:
        return redirect(request.url)

    file = request.files['image']

    if file.filename == '':
        return redirect(request.url)

    if file and allowed_file(file.filename):
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)
        prefix_to_remove = 'flasksnaja'
        User.query.filter_by(email=email).update({'pic': filename[len(prefix_to_remove):]})
        db.session.commit()
        flash("เปลี่ยนรูปโปรไฟล์สำเร็จ", category='success')
        return 'File uploaded successfully!'

    return 'Invalid file type!'
