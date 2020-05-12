from flask import Flask, render_template
from files import LoginForm
from collections import deque

app = Flask(__name__)

from app import routes

queue = deque()


@app.route('/')
def home():
    return render_template('templates/home.html')

if __name__ == '__main__':
    app.run(debug=True)