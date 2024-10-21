from maincode.users.forms import (RegistrationForm, LoginForm, UpdateAccount,
                                   RequestResetForm, ResetPasswordForm)
from maincode.users.utils import send_reset_email
from flask import render_template, request, Blueprint, flash
from maincode import db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required
from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from maincode.models import User
from maincode.models import Project


users = Blueprint('users', __name__)


@users.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash(f'Login successfull, welcome {current_user.username}', 'success')
            return redirect(url_for('main.home'))
        else:
            flash('Login unsuccessfull. Check username or password', 'danger')
    return render_template('login.html', title='Login', form=form)


@users.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    if User.query.filter_by(id=1).first():
        flash(f"Admin already registered", "warning")
        return redirect(url_for('main.home'))
    form=RegistrationForm()
    if form.validate_on_submit():
        if form.username.data in "ginonig":
            flash("Matteo sei brutto non puoi usare il mio sito", "danger")
            return redirect(url_for("main.home"))
        hashed_pw=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        login_user(user, remember=True)
        flash(f'Your account has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('register.html', title='Register', form=form)


@users.route('/logout')
def logout():
    logout_user()
    flash('Logged out successfully','info')
    return redirect(url_for('main.home'))
