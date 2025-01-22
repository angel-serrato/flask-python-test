from flask import Blueprint, render_template, request, redirect, url_for
from app.models.user_model import User

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')  # Definir correctamente el Blueprint

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('auth/login.html')

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user_model = User()
        existing_user = user_model.get_user_by_email(email)
        if existing_user:
            return 'User already exists', 400
        user_model.create_user(email, password)
        print('User created')
        return redirect(url_for('auth.login'))
    return render_template('auth/signup.html')

@auth_bp.route('/logout')
def logout():
    # Lógica de logout
    return redirect(url_for('auth.login'))

