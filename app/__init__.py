from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from authlib.integrations.flask_client import OAuth
from config import Config  # Use absolute import

db = SQLAlchemy()
oauth = OAuth()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # Load configurations from Config

    # Initialize extensions
    db.init_app(app)
    oauth.init_app(app)
    CORS(app, supports_credentials=True)

    # Import and register blueprints
    from .auth import auth_bp
    from .routes import bp as main_bp

    app.register_blueprint(auth_bp, url_prefix='/auth')  # Auth routes under /auth
    app.register_blueprint(main_bp, url_prefix='/api')    # Main routes under /api

    # Create database tables
    with app.app_context():
        db.create_all()

    return app
