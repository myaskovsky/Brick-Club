from flask import render_template, url_for, flash, redirect, request, Blueprint
from app.users.forms import SignInForm, SignUpForm

#from flask_login import login_user, current_user, logout_user, login_required
from app import db#, bcrypt
from app.models import User, Post
#from app.users.forms import (RegistrationForm, LoginForm, UpdateAccountForm,
#                                   RequestResetForm, ResetPasswordForm)
#from app.users.utils import save_picture, send_reset_email

users = Blueprint('users', __name__)


@users.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    form = SignUpForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('main.home'))
    return render_template('public/sign_up.html', title='Sign Up', form=form)


@users.route('/sign_in', methods=['GET', 'POST'])
def sign_in():
    form = SignInForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@mag.com' and form.password.data == 'password':
            flash('You have been logged in', 'success')
            return redirect(url_for('main.home'))
        else:
            flash('Login unsuccessful. Please check email and password', 'danger')
    return render_template('public/sign_in.html', title='Sign In', form=form)

