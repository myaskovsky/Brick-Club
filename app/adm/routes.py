from flask import Blueprint, request, render_template
from app import admins, db
from flask_admin.contrib.sqla import ModelView
from app.models import User, Post, Set
#from app.adm.utils import create_default_admin


#create_default_admin('admin', 'admin@test.com')

adm = Blueprint('adm', __name__)
admins.add_view(ModelView(User, db.session))
admins.add_view(ModelView(Post, db.session))
admins.add_view(ModelView(Set, db.session))




'''
@adm.route("/admin")
def admin_sign_up():
    return "Admin dashboard"
'''