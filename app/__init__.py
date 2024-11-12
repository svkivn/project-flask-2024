from flask import Flask


app = Flask(__name__)
#app.config.from_pyfile("../config.py")
app.config.from_object('config') #налаштування з файлу config.py

from . import views

from .posts import post_bp
from .users import bp as user_bp
app.register_blueprint(post_bp)
app.register_blueprint(user_bp, url_prefix="/users")
