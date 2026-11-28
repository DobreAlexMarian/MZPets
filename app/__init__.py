# __init__.py
"""MZPets Flask app package initialization"""

from flask import Flask


def create_app():
    app = Flask(__name__)
    # Register blueprints or routes here if using modular structure
    from . import routes
    app.register_blueprint(routes.main_bp)
    return app
