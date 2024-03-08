from flask import Flask
from routes import converter_bp

def create_app():
    app = Flask(__name__, template_folder='../templates')
    app.register_blueprint(converter_bp)
    return app
