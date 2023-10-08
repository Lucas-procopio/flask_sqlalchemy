from flask import Flask, request, redirect
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate

app = Flask(__name__) # Flask instance
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app) # SQLAlchemy instance

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=False, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    occupation = db.Column(db.String(40), unique=False, nullable=True)

    def __init__(self, id, name, email, occupation):
        self.id = id
        self.name = name
        self.email = email
        self.occupation = occupation
    
    def __repr__(self):
        return f"Updated user {self.name}"

migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run()