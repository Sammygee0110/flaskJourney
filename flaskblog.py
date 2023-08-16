from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config["SECRET_KEY"] = "05646efc442447eb4b24b6a554d10d17"

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

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template("register.html", title="Register", form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title="Login", form=form)

if __name__ == "__main__":
    app.run(debug=True)