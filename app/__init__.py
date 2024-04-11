from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.secret_key = '3155'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:admin@localhost/db_investimentos'

db = SQLAlchemy(app)