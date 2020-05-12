from flask import Flask, render_template, redirect, url_for
from files import LoginForm, MatchForm
from config import Config
from utils import find_match, find_new_match, remove_match

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/', methods=['GET', 'POST'])
def home():
    form = LoginForm()
    if form.validate_on_submit():
        name = form.username.data
        return redirect(url_for('matches', match=find_match(name), user=name))
    return render_template('home.html', form=form)

@app.route('/matches/<user>/<match>', methods=['GET', 'POST'])
def matches(user, match):
    form = MatchForm()
    if form.validate_on_submit():
        if form.again.data == True:
            return redirect(url_for('matches', user=user, match=find_new_match(user,match)))
        else:
            return redirect('/')
    return render_template('matches.html', user=user, match=match,form=form)

if __name__ == '__main__':
    app.run(debug=True)