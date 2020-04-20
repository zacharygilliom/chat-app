from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime as datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = '4c582851189d6b422bfa30a383cc2749'
db = SQLAlchemy(app)

from chat_app import routes