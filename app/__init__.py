from flask import Flask
from .routes import bp as routes

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='your_secret_key',
    )

    app.register_blueprint(routes)

    return app