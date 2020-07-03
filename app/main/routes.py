from flask import Blueprint, request, render_template
from flask_login import current_user
from app.models import Post, Set, Comment


main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():

    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)

    '''
    form = AddCommentForm()
    if form.validate_on_submit():
        if current_user.is_authenticated:
            comment = Comment(text=form.text.data, user=current_user, post=)
    '''

    return render_template("public/home.html", posts=posts, title='Home')


@main.route("/catalog")
def catalog():
    page = request.args.get('page', 1, type=int)
    sets = Set.query.order_by(Set.year.desc()).paginate(page=page, per_page=20)

    return render_template("public/catalog.html", sets=sets, title='Catalog')


@main.route("/profile")
def profile():
    return render_template("public/profile.html", title='Profile')


@main.route("/about")
def about():
    return render_template("public/about.html", title='About')