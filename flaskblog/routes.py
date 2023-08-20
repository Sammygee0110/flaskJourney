from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post
from flaskblog import app
from flask import render_template, url_for, redirect, flash

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts, title="Home Page")


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


@app.route("/about")
def about():
    return render_template("about.html", title="About Page")

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created succesfully for {form.username.data}!", "success")
        return redirect(url_for('home'))
    return render_template("register.html", title="Register", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@gmail.com" and form.password.data == "password":
            flash(f"Login successful", "success")
            return redirect(url_for('home'))
        else:
            flash("Login failed. Please check username and password!", "danger")
    return render_template("login.html", title="Login", form=form)