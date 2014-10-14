from flask import Flask
from app.core.admin import create_admin
from app.core.models import db
from flask.ext.login import LoginManager


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    register_database(app)
    register_blueprint(app)
    init_login(app)
    create_admin(app, db)
    return app


def register_log():
    import logging
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)


def register_database(app):
    db.init_app(app)
    db.app = app


def register_blueprint(app):
    from app.core.views import bp
    app.register_blueprint(bp)


# Initialize flask-login
def init_login(app):
    login_manager = LoginManager()
    login_manager.init_app(app)

    # Create user loader function
    @login_manager.user_loader
    def load_user(user_id):
        from app.core.models import User
        return db.session.query(User).get(user_id)





