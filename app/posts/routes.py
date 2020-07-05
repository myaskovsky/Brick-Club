from flask import render_template, url_for, flash, redirect, request, Blueprint
from app.users.forms import SignInForm, SignUpForm
from flask_login import login_user, current_user, logout_user, login_required
from app import db, bcrypt
from app.models import User, Post, Comment
from app.posts.forms import AddCommentForm


posts = Blueprint('posts', __name__)


@posts.route("/show_post/<int:post_id>", methods=['GET', 'POST'])
def show_post(post_id):
    post = Post.query.get_or_404(post_id)
    form = AddCommentForm()
    if form.validate_on_submit():
        comment = Comment(text=form.text.data, user=current_user, post=post)
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('posts.show_post', post_id=post.id, form=form))
    return render_template("public/post.html", post=post, form=form)
