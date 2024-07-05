from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from app.auth.forms import LoginForm, RegistrationForm
from app.models import User

auth = Blueprint('auth', __name__)

@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Logika untuk login
        pass
    return render_template("auth/login.html", title="Login", form=form)

@auth.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Logika untuk register
        pass
    return render_template("auth/register.html", title="Register", form=form)