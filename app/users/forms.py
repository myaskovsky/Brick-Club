from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import User


class SignUpForm(FlaskForm):
    username = StringField(validators=[DataRequired(), Length(min=2, max=20)], render_kw={"placeholder": "Username"})
    email = StringField(validators=[DataRequired(), Email()], render_kw={"placeholder": "Email"})
    password = PasswordField(validators=[DataRequired()], render_kw={"placeholder": "Password"})
    confirm_password = PasswordField(validators=[DataRequired(), EqualTo('password')],
                                     render_kw={"placeholder": "Confirm Password"})
    submit = SubmitField('Sign Up')


class SignInForm(FlaskForm):
    email = StringField(validators=[DataRequired(), Email()], render_kw={"placeholder": "Email"})
    password = PasswordField(validators=[DataRequired()], render_kw={"placeholder": "Password"})
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RequestResetForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()],  render_kw={"placeholder": "Email"})
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('There is no account with that email. You must register first.')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()], render_kw={"placeholder": "Password"})
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')], render_kw={"placeholder": "Confirm password"})
    submit = SubmitField('Reset Password')