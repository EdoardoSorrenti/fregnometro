from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_mail import Mail


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()


class Config:
    SECRET_KEY = "TommasoGay"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    login_manager.init_app(app)
    db.init_app(app)
    bcrypt.init_app(app)
    mail.init_app(app)

    from maincode.main.routes import main
    from maincode.users.routes import users
    from maincode.errors.handlers import errors

    app.register_blueprint(main)
    app.register_blueprint(users)
    app.register_blueprint(errors)

    return app
