"""Initialize Flask app."""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import conf

db = SQLAlchemy()


def create_app():
    """Construct the core application."""
    app = Flask(__name__,)
    app.config["SQLALCHEMY_DATABASE_URI"] = conf.postgres_url
    # Initialize Database Plugin
    db.init_app(app)

    with app.app_context():
        from . import routes  # Import routes

        db.create_all()  # Create database tables for our data models

        return app