
from config import  db, Note

def note(note_id):

    Note.query.filter_by(id = note_id ).delete()
    db.session.commit()

    return()
