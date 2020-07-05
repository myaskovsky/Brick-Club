from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError


class AddCommentForm(FlaskForm):
    text = StringField(validators=[DataRequired(), Length(min=1, max=300)], render_kw={"placeholder": "Your comment..."})
    submit = SubmitField('Add')
