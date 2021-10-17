from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy #For database
from flask_bcrypt import Bcrypt # Generating hash password
from flask_login import LoginManager, login_manager # To manage all the login systems for our webiste


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = '361dc60b89ca85ab7fa57842'
db = SQLAlchemy(app) # Create an instance of SQLAlchemy
bcrypt = Bcrypt(app) # Create an instance of Bcrypt
login_manager = LoginManager(app) # creaye an instance of LoginManager
login_manager.login_view = "login_page" # This will take the users to login page after they click lets get started on home page
login_manager.login_message_category = "info" # for better display of the message

from market import routes