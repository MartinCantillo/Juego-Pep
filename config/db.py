from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/db_playpep'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = 'pep05052023'

bd = SQLAlchemy(app)
ma = Marshmallow(app)