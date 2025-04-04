from flask import Flask
from .routes import bp as routes
from .logging import setup_logging

def create_app():
    # Congirue app logging
    setup_logging()

    # Create Flask app
    app = Flask(__name__)

    app.register_blueprint(routes)

    return app