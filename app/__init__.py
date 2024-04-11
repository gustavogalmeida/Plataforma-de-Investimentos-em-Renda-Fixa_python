from flask import Flask

app = Flask(__name__)
app.secret_key = '3155'

from app import views
