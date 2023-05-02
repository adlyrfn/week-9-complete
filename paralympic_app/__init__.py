from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from paralympic_app.config import Config


# Create a global SQLAlchemy object
db = SQLAlchemy()
# Create a global Flask-Marshmallow object
ma = Marshmallow()


def create_app(config_pbject=Config):
    """Create and configure the Flask app"""
    app = Flask(__name__)
    # Config parameters are in config.py
    app.config.from_object(config_pbject)

    # Uses a helper function to initialise extensions
    initialize_extensions(app)


    with app.app_context():
        from paralympic_app.models import Event, Region
        # Include the routes from routes.py
        from paralympic_app import routes

        db.create_all()

    return app


def initialize_extensions(app):
    """Binds extensions to the Flask application instance (app)"""
    # Flask-SQLAlchemy
    db.init_app(app)
    # Flask-Marshmallow
    ma.init_app(app)
