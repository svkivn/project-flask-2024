from flask import request, render_template, current_app

# from . import app

@current_app.route('/')
def main():
    return render_template("base.html")

@current_app.route('/homepage') 
def home():
    """View for the Home page of your website."""
    agent = request.user_agent

    return render_template("home.html", agent=agent)


