from flask_login import login_user, current_user
from config import bcrypt, User
from flask import request

def login(email, password):

    user = User.query.filter_by(email = email).first()
    if user and bcrypt.check_password_hash(user.password, password):
        login_user(user)

    return()
