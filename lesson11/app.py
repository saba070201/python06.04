from flask import Flask,render_template,url_for,redirect,request
from flask_sqlalchemy import SQLAlchemy
from models import * 
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
db = SQLAlchemy()
db.init_app(app)

@app.route('/')
def home():
    data=db.session.execute(db.select(Notes)).scalars()
    return render_template('index.html',data=data)


@app.route('/note-<int:note_id>')
def note(note_id):
    note_data=db.get_or_404(Notes,note_id)
    return render_template('note.html',note_data=note_data)

@app.route('/create-note')
def create_note():
    note=Notes(title='title',memo='memo',important=1)
    db.session.add(note)
    db.session.commit()
    return redirect(url_for('note',note_id=note.id))

@app.route('/delete-note-<int:note_id>')
def delete_note(note_id):
    note=db.get_or_404(Notes,note_id)
    db.session.delete(note)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/change-note-<int:note_id>',methods=['GET','POST'])
def change_note(note_id):
    note=db.get_or_404(Notes,note_id)
    if request.method=='POST':
        note.title=request.form.get('title_data')
        note.memo=request.form.get('memo_data')
        db.session.commit()
    return redirect(url_for('home'))
if __name__=='__main__':
    app.run(debug=True)

