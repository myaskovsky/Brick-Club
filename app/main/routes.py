from flask import Blueprint, request, render_template
from app.models import Post, Set

main = Blueprint('main', __name__)

'''
posts = [
    {
        'title': 'Post 1',
        'content': 'First content',
        'date_posted': 'April 5, 2020'
    },
    {
        'title': 'Post 2',
        'content': 'Second content',
        'date_posted': 'April 9, 2020'
    },
    {
        'title': 'Post 3',
        'content': 'Third Content',
        'date_posted': 'April 15, 2020'
    },
    {
        'title': 'Post 4',
        'content': 'Fourth Content',
        'date_posted': 'April 16, 2020'
    },
    {
        'title': 'Post 5',
        'content': 'Fifth Content',
        'date_posted': 'April 16, 2020'
    }
]

sets = [
    {
        'article': '75019',
        'name': 'AT-TE',
        'age': '12+',
        'season': 'summer 2020',
        'price': '100$',
        'pieces': '360',
        'description': 'AT-TE is a republic armored vehicle'
    },
{
        'article': '75019',
        'name': 'AT-TE',
        'age': '12+',
        'season': 'summer 2020',
        'price': '100$',
        'pieces': '360',
        'description': 'AT-TE is a republic armored vehicle'
    },
{
        'article': '75019',
        'name': 'AT-TE',
        'age': '12+',
        'price': '100$',
        'pieces': '360',
        'description': 'AT-TE is a republic armored vehicle'
    },
    {
        'article': '75019',
        'name': 'AT-TE',
        'age': '12+',
        'season': 'summer 2020',
        'price': '100$',
        'pieces': '360',
        'description': 'AT-TE is a republic armored vehicle'
    }
]
'''

comments = [
    {
        'author': 'John',
        'text': 'Where is my dog?'
    },
    {
        'author': 'Manager',
        'text': 'On the reception, Sir'
    }
]


@main.route("/")
@main.route("/home")
def home():
    # TODO: create profile page, add posts and sets to db,
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template("public/home.html", posts=posts, comments=comments, title='Home')


@main.route("/catalog")
def catalog():
    page = request.args.get('page', 1, type=int)
    sets = Set.query.order_by(Set.year.desc()).paginate(page=page, per_page=5)
    return render_template("public/catalog.html", sets=sets, title='Catalog')


@main.route("/profile")
def profile():
    return render_template("public/profile.html", title='Profile')


@main.route("/about")
def about():
    return render_template("public/about.html", title='About')