from flask import Flask
from flask_sqlalchemy import SQLAlchemy

restore=Flask(__name__)

restore.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////media/nahid/Projects/MarvinAi/dataset_creator/marvin.db'

db=SQLAlchemy(restore)

class Marvin(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    speaker=db.Column(db.Text)
    reply=db.Column(db.Text)
    tag=db.Column(db.Text)

#db.create_all()

print(Marvin.query.all())
