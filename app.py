from flask import Flask, render_template
from files import LoginForm
from config import Config
from utils import find_match, find_new_match, remove_match

app = Flask(__name__)
app.config.from_object(Config)

from app import routes

@app.route('/')
def home():
    form = LoginForm()
    if form.validate_on_submit():
        name = form.username.data
        return redirect(url_for('matches', user=name, match=find_match(name)))
    return render_template('home.html', form=form)

@app.route('/matches/<user>/<match>')
def matches(user, match=None):
    if form.validate_on_submit():
        if form.again.data == True:
            return render_template('matches.html', user=user, match=find_new_match(user))
        else:
            return redirect('/')
    return render_template('matches.html', user=user, match=match)

if __name__ == '__main__':
    app.run(debug=True)