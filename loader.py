from flask_sqlalchemy import SQLAlchemy
from config import sqlite_path
from flask import Flask


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = sqlite_path
db = SQLAlchemy(app)
