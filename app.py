from flask import Flask, render_template
from files import LoginForm
from collections import deque

app = Flask(__name__)

from app import routes

queue = deque()
matches = {}

@app.route('/')
def home():
    if form.validate_on_submit():
        name = form.username.data
        if name not in matches:
            matches[name] = None
        if matches[name] != None:
            return redirect(url_for('matches', user=name, match=matches[name]))
        if not queue:
            queue.append(name)
            return redirect(url_for('matches', user=name))
        if queue[0] == name:
            return redirect(url_for('matches', user=name))
        else:
            match = queue.popleft()
            matches[match] = name
            matches[name] = match
            return redirect(url_for('matches', user=name, match=match))
    return render_template('templates/home.html')

@app.route('/matches/<user>/<match>')
def matches(user, match=None):
    return render_template('templates/matches.html', user=user, match=match)

if __name__ == '__main__':
    app.run(debug=True)