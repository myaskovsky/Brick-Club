from flask import Blueprint, render_template

main = Blueprint('main', __name__)

#username = 'Yaroslav'
#username =  None

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
    }
]


@main.route("/")
@main.route("/home")
def home():
    return render_template("public/home.html", posts=posts, title='Home')


@main.route("/catalog")
def catalog():
    return render_template("public/catalog.html", sets=sets, title='Catalog')


@main.route("/profile")
def profile():
    return render_template("public/profile.html", title='Profile')


@main.route("/about")
def about():
    return render_template("public/about.html", title='About')