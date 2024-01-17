
from config import app, db, bcrypt, User, Note
from flask import Flask, render_template, request, redirect, url_for
from flask_login import  current_user, logout_user, login_required
import forms
import sys
sys.path.append('backend/CRUD')
import create
import update
import delete
import actions

@app.route('/', methods = ['GET','POST'])
@app.route('/index', methods = ['GET','POST'])
def hello_world():

    # if there is a register request
    if forms.RegistrationForm().validate_on_submit():
        create.user(forms.RegistrationForm())
        actions.login(forms.RegistrationForm().email.data,
                                  forms.RegistrationForm().password.data)
        return redirect(url_for('hello_world'))

    # If there is a login request
    if forms.LoginForm().validate_on_submit():
        actions.login(forms.RegistrationForm().email.data,
                                  forms.RegistrationForm().password.data)
        return redirect(url_for('hello_world'))

    # If there is a request to logout the current user
    if (request.method == "POST") & (request.form.get('post_header') == 'log out'):
        logout_user()
        return redirect(url_for('hello_world'))

    # if there is a request to create or update a note
    if forms.NoteForm().validate_on_submit():
        if request.form.get('post_header') == 'update note':
            update.note(forms.NoteForm())
        else:
            create.note(forms.NoteForm())
        return redirect(url_for('hello_world'))

    # If there is a request to delete a note
    if (request.method == "POST") & (request.form.get('post_header') == 'delete note'):
        delete.note(request.form.get('note_to_delete'))
        return redirect(url_for('hello_world'))

    # Getting all needed database objects
    if current_user.is_authenticated:
        notes = Note.query.filter_by(username = current_user.username).all()
    else:
        notes = []

    return render_template('index.html',
                           notes = notes,
                           login_form = forms.LoginForm(),
                           register_form = forms.RegistrationForm(),
                           csrf_form = forms.csrf_form(),
                           note_form = forms.NoteForm())
