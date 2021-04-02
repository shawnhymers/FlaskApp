
from config import  db, Note
from flask import request

def note(note_form):

    Note.query.filter_by(id = request.form.get('note_to_update')).update({
                  'note' : note_form.note.data,
                  'boolean' : note_form.boolean.data,
                  'float' : note_form.float.data,
                  'date' : note_form.date.data})
    db.session.commit()

    return()
