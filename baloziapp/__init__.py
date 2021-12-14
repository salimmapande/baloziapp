from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
#from flask_bootstrap import Bootstrap
#from flask_datepicker import datepicker
#from flask_migrate import Migrate#, MigrateCommand
#from flask_script import Manager
#from flask_login import LoginManager



app =  Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tamisys.db'
app.config['SECRET_KEY'] = 'be552397e7c00ccad73ea6b3'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

#bootstrap = Bootstrap(app)
#migrate = Migrate(app, db)
#manager = Manager(app)
#manager.add_command('db', MigrateCommand)
#login_manager = LoginManager(app)
#login_manager.login_view = "login_page"

from baloziapp import routes
from baloziapp import first_build