from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

app = Flask(__name__)
app.config.from_object('config')
# for gunicorn
from werkzeug.contrib.fixers import ProxyFix
app.wsgi_app = ProxyFix(app.wsgi_app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


db = SQLAlchemy(app)

from app import views, models
