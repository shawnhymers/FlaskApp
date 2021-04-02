
from config import app, db, bcrypt, User
from flask import Flask, render_template, request, redirect, url_for
from flask_login import login_user, current_user, logout_user, login_required
import forms

@app.route('/', methods = ['GET','POST'])
@app.route('/index', methods = ['GET','POST'])
def hello_world():

    # Creating a new user when the register form validates
    if forms.RegistrationForm().validate_on_submit():
        # Creating a new user in the database
        register_form = forms.RegistrationForm()
        hashed_password = bcrypt.generate_password_hash(register_form.password.data).decode('utf-8')
        user = User(username = register_form.username.data,
                    email = register_form.email.data,
                    password = hashed_password)

        db.session.add(user)
        db.session.commit()
    # Signing in the user after creating them
        user = User.query.filter_by(email = forms.RegistrationForm().email.data).first()
        if user and bcrypt.check_password_hash(user.password, forms.RegistrationForm().password.data):
            login_user(user)
        # Taking the user to the authenticated side of the site
            return redirect(url_for('hello_world'))

    if forms.LoginForm().validate_on_submit():
        user = User.query.filter_by(email = forms.LoginForm().email.data).first()
        if user and bcrypt.check_password_hash(user.password, forms.LoginForm().password.data):
            login_user(user, remember = forms.LoginForm().remember.data)

            return redirect(url_for('hello_world'))

    if (request.method == "POST") & (request.form.get('post_header') == 'log out'):
        logout_user()
        return redirect(url_for('hello_world'))


    return render_template('index.html',
                           login_form = forms.LoginForm(),
                           register_form = forms.RegistrationForm())
