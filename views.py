from flask import render_template, redirect, url_for, request, session
from models.users import User
from common.database import Database
from common.utils import Util
from common import decorators
from __init__ import app

@app.before_first_request
def initialize_database():
    Database.initialize('blog')

@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        existing_user = Database.find_one('user_data', {'username': username})
        if existing_user is None:
            password = request.form['password']
            password_confirm = request.form['password_confirm']
            if password != password_confirm:
                error = "Passwords do not match."
                return render_template('register.html', title='register', error=error)
            else:
                password = Util.hash_password(password)
                new_user = User(username=username, password=password)
                new_user.save_to_database()
                return redirect(url_for('login'))
        else:
            error = "Username has already been taken."
    return render_template('register.html', title='register', error=error)

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == "POST":
        session['username'] = request.form['username']
        user_password = request.form['password']
        user_data = User.find_username(session['username'])
        if request.form['username'] != user_data['username'] or Util.check_hashed_password(password=user_password, hashed_password=user_data['password']) is False:
            error = "Invalid Credentials."
            session['username'] = None
        else:
            return redirect(url_for('home'))
    return render_template('login_page.html', error=error, title='login')

@app.route('/logout')
def signout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/home', methods=["GET", "POST"])
@decorators.login_required
def home():
    return render_template('dashboard.html', title='dashboard')
