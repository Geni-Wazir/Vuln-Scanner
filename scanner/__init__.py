from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_admin import Admin
from configparser import ConfigParser
from flask_migrate import Migrate

app = Flask(__name__)

    
app.config['SECRET_KEY'] = '3fd5f6f457adc67ee57d46373dc1b62d7d26a543'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://scanner:scanner@db/scanner'


db = SQLAlchemy(app)


migrate=Migrate()

migrate.init_app(app, db)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
admin = Admin(app, name='Admin')
parser = ConfigParser()
parser.read('config.ini')


def get_admin():
    return parser.get('APP','ADMINS')

# # from automate_pentest import routes