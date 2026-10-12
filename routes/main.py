from flask import Blueprint, render_template, request, session
from app.models import User
main = Blueprint('main', __name__)


@main.route("/")

def home():
    return render_template("home.html")

@main.route("/login", methods=["GET", "POST"])

def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        user = User.query.filter_by(username=username).first()

        if user and user.password == password:
            session[username] = user.id
            return f"Login successful! Your user ID is: {user.id}"
        else:
            return "Invalid username or password."
    return render_template("auth/login.html")

