from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder='static', static_url_path='/static')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:admin@localhost/db_plataforma_investimentos'
db = SQLAlchemy(app)

from app import views