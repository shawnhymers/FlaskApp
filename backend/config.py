
# Importing the flask class
from flask import Flask

# Making an isntance of the Flask Class (THis will get passed to app.py)
app = Flask(__name__, template_folder='../templates')
