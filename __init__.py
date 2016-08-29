import os
from flask import Flask
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)  # '__main__'
app.secret_key = "my secret key"

import views