from datetime import datetime
from flask import Flask, render_template, url_for, redirect, flash
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SECRET_KEY"] = "05646efc442447eb4b24b6a554d10d17"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship("Post", backref="author", lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"
    
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}', '{self.content}')"

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

if __name__ == "__main__":
    app.run(debug=True)