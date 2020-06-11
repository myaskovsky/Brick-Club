from app.models import User
from app import db, bcrypt




'''
def create_default_admin(username, email, password):
    if User.query.filter_by(username='admin').first():
        print('Default admin exist')
    else:
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        user = User(username, email, hashed_password, admin=True)
        db.session.add(user)
        db.session.commit()
'''