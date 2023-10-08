from flask import Flask, request, redirect
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate

app = Flask(__name__) # Flask instance
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app) # SQLAlchemy instance

#Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=False, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    occupation = db.Column(db.String(40), unique=False, nullable=True)

    def __repr__(self):
        return f"Updated user {self.name}"

migrate = Migrate(app, db)

#function to render index page
@app.route('/')
def index():
    profiles = User.query.all()
    return render_template('index.html', profiles=profiles)

@app.route('/add_data')
def add_data():
    return render_template('add_profiles.html')

@app.route('/add', methods=["POST"])
def profile():
    name = request.form.get('name')
    email = request.form.get('email')
    occupation = request.form.get('occupation')

    if name != '' and email != '':
        profile = User(name=name, email=email, occupation=occupation)
        db.session.add(profile)
        db.session.commit()
        return redirect('/')
    else:
        return redirect('/')

if __name__ == '__main__':
    app.run()
