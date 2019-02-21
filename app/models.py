from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

class User(UserMixin,db.Model):
    __tablename__='users'

    id = db.Column(db.Integer,primary_key =True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index =True)
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))
    pass_secure  = db.Column(db.String(255))
    
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
    

    def __repr__(self):
        return f'User {self.username}'

# class Intrest(db.Model):
#     __tablename__='intrests'

#     id = db.Column(db.Integer,primary_key = True)
#     intrest_name = db.Column(db.String)
#     description = db.Column(db.String)
    

# class UserIntrests(db.Model):

#     __tablename__ ='user_intrests'

#     id = db.Column(db.Integer,primary_key = True)
#     user_id = db.Column(db.Integer("user.id"))
#     intrest_id = db.Column(db.Integer,db.ForeignKey("intrest.id"))
    

#     def save_comment(self):
#         db.session.add(self)
#         db.session.commit()

#     def __repr__(self):
#         return f"Comment('{self.comment}', '{self.posted}')"
