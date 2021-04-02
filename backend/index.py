
from config import app
from flask import Flask, render_template
@app.route('/')
@app.route('/index')
def hello_world():
    return render_template('index.html')
