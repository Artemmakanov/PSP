"""Initialize Flask app."""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import conf

db = SQLAlchemy()


def create_app():
    """Construct the core application."""
    app = Flask(__name__,)
    app.config["SQLALCHEMY_DATABASE_URI"] = conf.postgres_url
    
    def add_cors_headers(response):
        response.headers['Access-Control-Allow-Origin'] = '*'  # Adjust as needed
        response.headers['Access-Control-Allow-Credentials'] = 'true'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
        return response
    
    @app.after_request
    def after_request(response):
        return add_cors_headers(response)
    
    # Initialize Database Plugin
    db.init_app(app)

    with app.app_context():
        from . import routes  # Import routes

        db.create_all()  # Create database tables for our data models

        return app