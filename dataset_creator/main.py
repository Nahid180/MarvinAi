from flask import Flask,render_template,redirect,request
from flask_sqlalchemy import SQLAlchemy
import json


app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:khan2019@localhost/marvin?charset=utf8mb4'

db=SQLAlchemy(app)

class Marvin(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    speaker=db.Column(db.Text)
    reply=db.Column(db.Text)
    tag=db.Column(db.Text)

with open("/media/nahid/Projects/MarvinAi/dataset_creator/static/config.json",'rb') as f:
    file=json.load(f)

@app.route('/')
def home():
    get=Marvin.query.all()
    tag=file['Tag']
    return render_template('index.html',data=get,tag=tag)

@app.route('/change-tag', methods=['GET','POST'])
def change_tag():
    tag=request.form['tag']
    file['Tag']=tag
    print(tag)
    with open("static/config.json",'w') as writer:
        json.dump(file,writer,indent=2)
    return redirect('/')

@app.route('/save-data',methods=['POST'])
def saveData():
    speaker=request.form['speaker']
    reply=request.form['reply']
    tag=request.form['tag']
    db.session.add(Marvin(speaker=speaker,reply=reply,tag=tag))
    db.session.commit()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)