from flask import render_template, url_for, flash, redirect, request, Blueprint
from app.users.forms import SignInForm, SignUpForm
from flask_login import login_user, current_user, logout_user, login_required
from app import db, bcrypt
from app.models import User, Post
from app.users.forms import (SignUpForm, SignInForm)#, UpdateAccountForm,
                                  #RequestResetForm, ResetPasswordForm)
#from app.users.utils import save_picture, send_reset_email

users = Blueprint('users', __name__)


@users.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = SignUpForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('users.sign_in'))
    return render_template('public/sign_up.html', title='Sign Up', form=form)


@users.route('/sign_in', methods=['GET', 'POST'])
def sign_in():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = SignInForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            #flash('You have been logged in', 'success')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash('Login unsuccessful. Please check email and password', 'danger')
    return render_template('public/sign_in.html', title='Sign In', form=form)


@users.route("/sign_out")
def sign_out():
    logout_user()
    return redirect(url_for('main.home'))
