"""
app.py
Application entry point. Creates the Flask app and registers the
controller blueprint. Run with: python app.py
"""

from flask import Flask
from controllers.main_controller import main_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(main_bp)
    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True, port=5000)
