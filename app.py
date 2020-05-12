from flask import Flask, render_template
from files import LoginForm
from collections import deque
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import routes

queue = deque()
matches = {}

find_match(name):
    if name not in matches:
        matches[name] = None
    if not queue:
        queue.append(name)
        return None
    if queue[0] == name:
        return None
    if matches[name] != None:
        return matches[name]
    else:
        match = queue.popleft()
        matches[match] = name
        matches[name] = match
        return match

remove_match(name, match):
    matches[name] = None
    matches[match] = None

find_new_match(name, match):
    remove_match(name, match)
    return find_match(name, match)

@app.route('/')
def home():
    form = LoginForm()
    if form.validate_on_submit():
        name = form.username.data
            return redirect(url_for('matches', user=name, match=matches[name]))
            return redirect(url_for('matches', user=name, match=match))
    return render_template('templates/home.html', form = form)

@app.route('/matches/<user>/<match>')
def matches(user, match=None):
    if request.method == 'POST':
        if request.form.name == 'tryagain':
            return render_template('templates/matches.html', user=user, match=find_new_match(user))
        if request.form.name == 'exit':
            return redirect('/')
    return render_template('templates/matches.html', user=user, match=match)

if __name__ == '__main__':
    app.run(debug=True)