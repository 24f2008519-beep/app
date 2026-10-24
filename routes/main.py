from flask import Blueprint, render_template, request, session, redirect, url_for
from app.models import User
from app import db
main = Blueprint('main', __name__)


@main.route("/home")

def home():
    return render_template("home.html")

@main.route("/", methods=["GET", "POST"])

def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        user = User.query.filter_by(username=username).first()

        if user and user.password == password:
            session["user_id"] = user.id
            return f"Login successful! Your user ID is: {user.id}"
        else:
            return "Invalid username or password."
    return render_template("auth/login.html")


@main.route("/logout")
def logout():
    session.pop("user_id", None)
    return redirect(url_for("main.home"))

@main.route("/profile")
def profile():
       
    user_id = session.get("user_id")
    if user_id is None:
        return "User not found. Please log in first."
            
    user = User.query.filter_by(id=user_id).first()
    if user is None:
        return "User not found."


    return render_template("auth/profile.html", user=user)

@main.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        existing_user = User.query.filter(
            (User.username == username) |
            (User.email == email)
        ).first()

        if existing_user:
            return "Username or email already registered."

        
        new_user = User(username=username, 
                        email=email, password=password, 
                        role='student')
        db.session.add(new_user)
        db.session.commit()

        
        return redirect(url_for("main.login")) 
    return render_template("auth/register.html")


@main.route("/examiner/register", methods=["GET", "POST"])
def examiner_register():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        existing_user = User.query.filter(
           (User.username == username) |
           (User.email == email)
        ).first()

        if existing_user:
            "Username or email already registered."

        new_user = User(username=username, 
                        email=email, password=password, 
                        role='student')
        db.session.add(new_user)
        db.session.commit()
        return "Registration successful. Awaiting admin approval."
    return render_template("auth/examiner_register.html")