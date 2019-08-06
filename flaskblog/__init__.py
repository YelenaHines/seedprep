from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


app = Flask(__name__)
#app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SECRET_KEY'] = 'ea69ec53427e14055be018838265178c'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
#db = SQLAlchemy(app)
bcrypt= Bcrypt(app)

from flaskblog import routes
