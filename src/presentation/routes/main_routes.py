from flask import Blueprint

main_bp = Blueprint('main_bp', __name__)

@main_bp.route('/')
def home():
    return "<h2>Welcome to Secure User Authentication System</h2><p><a href='/register'>Register</a> | <a href='/login'>Login</a></p>"
