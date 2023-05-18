from flask import Flask,render_template,url_for
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



if __name__=='__main__':
    app.run(debug=True)

