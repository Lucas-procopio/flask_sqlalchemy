# Using Flask to connect a SQLAlchemy


### Install libs using pip package:
    1° Creating a environment. (ps: env, venv, environ or others).

    2° Then, run in environment terminal:
    
    ˋˋˋ
    pip install -r requirements.txt
    ˋˋˋ 
        
    OBS: Check if pip package is uninstall. If uninstal, see how to install in:
        https://pip.pypa.io/en/stable/cli/pip_install/
    
<br>

### Tools Used:
    - Flask 3.0.0 Framework
    - Flask SQLAlchemy 3.1.1 extension
    - Flask migrate 4.0.5 extension
    - SQLAlchemy database


### Initialize Flask app instance<br>
° Creating a app.py<br>
° Create Flask instance<br>
° Define SQLALCHEMY_DATABASE_URI configure<br><br>

### Initialize SQLAlchemy instance<br>
° Passing a app variable with SQLALCHEMY_DATABASE_URI configuration.<br>
° Create database instance.<br><br>

### Define models

* Models are objects that represents tables.<br>
    * User table
        - id : Integer type; primary key.
        - name : String(20) type;
        - email : String(50) type; unique data.
        - occupation : String(40) type; nullable data.

<br>

### Creating Database

1° Using terminal, to run 'python'. <br>
2° Then, input:
    
    ˋˋˋ
    from app import db
    db.create_all()
    ˋˋˋ
3° It will create a new file called 'site.db'. <br><br>


## Migration on database

- Setting for migration in the code:

    migrate = Migrate(app, db)

    - Passing app and db instances.

- Run (terminal):

        ˋˋˋ 
        flask db init (for initialize flask database)
    
        flask db migrate -m 'Initial migration' (for start migration)
    
        flask db upgrade (for update flask)
        ˋˋˋ

<br>

### Define forms


1° Create index.html, with initial page. <br>
2° Creating forms page. <br>


## Creating routes:

    - There are 4 routes:
        1° index route: for index.
            http://localhost:5000/
        2° add_data: for render forms.
            http://localhost:5000/add_data
        3° profile: commit new data in database.
            http://localhost:5000/add
        4° erase: using to delete data.
            http://localhost:5000/delete/id


#### Comments:
    - To access http://localhost:5000