from flask import Flask, request, redirect, url_for, current_app
app = Flask(__name__, instance_relative_config=True)    # Construct an instance of Flask class for our webapp

app.config.from_pyfile("config.py", silent=True)
# app.config.from_object("config")

from . import views

