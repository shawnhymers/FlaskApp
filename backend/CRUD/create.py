
from config import  bcrypt, User, db, Note
from flask_login import current_user

def user(register_form):

    hashed_password = bcrypt.generate_password_hash(register_form.password.data).decode('utf-8')
    user = User(username = register_form.username.data,
                email = register_form.email.data,
                password = hashed_password)

    db.session.add(user)
    db.session.commit()

    return()

def note(note_form):

    note = Note(username = current_user.username,
                note = note_form.note.data,
                boolean = note_form.boolean.data,
                float = note_form.float.data,
                date = note_form.date.data)
    db.session.add(note)
    db.session.commit()

    return()
