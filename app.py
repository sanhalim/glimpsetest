from flask import Flask, render_template
from files import LoginForm
from collections import deque

app = Flask(__name__)

from app import routes

queue = deque()

@app.route('/')
def home():
    if form.validate_on_submit():
        return 
    return render_template('templates/home.html')

@app.route('/<user>+<match>')
def matches(user, match):
    if form.validate_on_submit():
        return
    return render_template('templates/matches.html')

if __name__ == '__main__':
    app.run(debug=True)