from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) # Flask instance
app.debug = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app) # SQLAlchemy instance

if __name__ == '__main__':
    app.run()