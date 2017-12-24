import os

from flask import Flask, redirect, render_template, request, session, url_for

from scoreboard import db_access
from scoreboard.auth import login_required

app = Flask(__name__)

app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-key')

PASSWORD = os.environ.get('SCOREBOARD_PASSWORD', 'password')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/player/list')
@login_required
def list_players():
    players = db_access.get_players()
    return render_template('player/list.html', players=players)


@app.route('/player/delete/<player_id>')
@login_required
def delete_player(player_id):
    db_access.delete_player(player_id)
    return redirect(url_for('list_players'))


@app.route('/player/add', methods=['POST'])
@login_required
def add_player():
    name = request.form.get('name')
    db_access.add_player(name)
    return redirect(url_for('list_players'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if PASSWORD == request.form['password']:
            session['authorized'] = 'yes'
            if request.form['next']:
                return redirect(request.form['next'])
            return redirect(url_for('index'))

    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('authorized', None)
    return redirect(url_for('index'))
