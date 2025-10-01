from flask import Blueprint, render_template, request, redirect
from src.application.services.auth_service import register_user, login_user

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        return register_user(request.form)
    return render_template('register.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return login_user(request.form)
    return render_template('login.html')