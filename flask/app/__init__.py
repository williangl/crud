from flask import Flask
from flask_migrate import Migrate

from .users import bp_user
from .model import configure as config_db
from .serealizer import configure as config_ma


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/crud.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    config_db(app)
    config_ma(app)

    Migrate(app, app.db)

    app.register_blueprint(bp_user)

    return app
