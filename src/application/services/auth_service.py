from flask import redirect
from src.infrastructure.mysql.user_repository import save_user, find_user
from src.infrastructure.mongodb.log_repository import log_attempt
import bcrypt

def register_user(form):
    username = form['username']
    email = form['email']
    password = bcrypt.hashpw(form['password'].encode('utf-8'), bcrypt.gensalt())
    save_user(username, email, password)
    return redirect('/login')

def login_user(form):
    username = form['username']
    password = form['password']
    user = find_user(username)
    if user and bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
        log_attempt(username, True)
        return "Login successful"
    else:
        log_attempt(username, False)
        return "Login failed"