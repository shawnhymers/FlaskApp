
from flask import Flask
from flask_login import UserMixin, current_user, login_manager
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import os
from flask_wtf.csrf import CSRFProtect
from flask_bcrypt import Bcrypt

# Making an isntance of the Flask Class (THis will get passed to app.py)
app = Flask(__name__,  template_folder='../templates')

bcrypt = Bcrypt(app)

# Adding cross site forgery protection
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
csrf = CSRFProtect(app)

# User authentication set up
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Database config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

# Data base object configuration
class User(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique = True, nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    password = db.Column(db.String(60), nullable = False)

class Note(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), nullable = False)
    note = db.Column(db.String(800), nullable = False)
    boolean = db.Column(db.Boolean, unique=False, default = False)
    float = db.Column(db.Float, nullable = False)
    date = db.Column(db.Date, nullable = False)
