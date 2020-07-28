from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from flask_login import UserMixin
from app import db, login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    admin = db.Column(db.Boolean, default=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def is_admin(self):
        return self.admin

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    comments = db.relationship('Comment', backref='title', lazy='dynamic')

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref='author', lazy=True)

    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    post = db.relationship('Post', backref='post', lazy=True)

    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    text = db.Column(db.String(140), nullable=False)

    def __repr__(self):
        return f"Comment('{self.text}', '{self.date_posted}')"


class Set(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    article = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(30), nullable=False)
    set_image = db.Column(db.String(20), nullable=False, default='set_default.jpg')
    year = db.Column(db.Integer, nullable=False)
    season = db.Column(db.String(10), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    pieces = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    in_stock = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"Set('{self.article}', '{self.name}', '{self.year}', '{self.price}')"

