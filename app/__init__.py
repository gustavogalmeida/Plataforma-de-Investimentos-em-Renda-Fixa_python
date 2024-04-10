from flask import Flask
import sqlalchemy

app = Flask(__name__)
db = sqlalchemy(app)


