from flask import session, render_template, redirect, url_for, request
from functools import wraps

def login_required(f):
	@wraps(f)
	def decorated_function(*args, **kwargs):
		error = None
		if 'username' not in session or session['username'] is None:
			error = "You must log in first."
			return render_template('login_page.html', error=error)
		return f(*args, **kwargs)
	return decorated_function