from flask import render_template, url_for, redirect, flash, request
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post
from flask_login import login_user, logout_user, current_user, login_required


posts = [
    {
        "author":"Samuel Mosebolatan",
        "date_posted": "14th of August 2023",
        "title": "Blog Post 1",
        "content": "First blog post content"
    },
    {
        "author": "Joshua Mosebolatan",
        "date_posted": "15th of August 2023",
        "title": "Blog Post 2",
        "content": "Second blog post content"
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts, title="Home Page")


@app.route("/about")
def about():
    return render_template("about.html", title="About Page")

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        app.app_context().push()
        db.create_all()
        db.session.add(user)
        db.session.commit()
        flash(f"Account created succesfully for {form.username.data}, you can now login", "success")
        return redirect(url_for('login'))
    return render_template("register.html", title="Register", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get("next")
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash("Login failed. Please check email and password!", "danger")
    return render_template("login.html", title="Login", form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))

@app.route("/account")
@login_required
def account():
    image_file = url_for('static', filename=f"profile_pic/{current_user.image_file}")
    return render_template('account.html', title='Account', image_file=image_file)