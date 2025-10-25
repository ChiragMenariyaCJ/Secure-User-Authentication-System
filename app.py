import os
from flask import Flask
from config import Config
from extensions import mysql, mongo_client

template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src', 'templates')
app = Flask(__name__, template_folder=template_dir)
app.config.from_object(Config)


# Initialize extensions
mysql.init_app(app)
mongo_db = mongo_client["auth_logs"]

# Import routes
from src.presentation.routes.auth_routes import auth_bp
app.register_blueprint(auth_bp)

from src.presentation.routes.main_routes import main_bp
app.register_blueprint(main_bp)

if __name__ == "__main__":
    app.run(debug=False)