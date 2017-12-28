from collections import namedtuple
import os

from flask import flash, Flask, redirect, render_template, request, session, url_for

from scoreboard import db_access, match_service
from scoreboard.auth import login_required

app = Flask(__name__)

app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-key')

PASSWORD = os.environ.get('SCOREBOARD_PASSWORD', 'password')

PlayerInput = namedtuple('Player', 'name')


@app.route('/')
def index():
    players = db_access.get_players()
    matches = db_access.get_matches()
    return render_template('index.html', players=players, matches=matches)


@app.route('/match/add', methods=['POST'])
@login_required
def add_match():
    match_input = match_service.build_match(
        request.form.get('player1'),
        request.form.get('player2'),
        int(request.form.get('score1')),
        int(request.form.get('score2'))
    )
    db_access.add_match(match_input)
    return redirect(url_for('index'))


@app.route('/match/delete/<match_id>')
@login_required
def delete_match(match_id):
    db_access.delete_match(match_id)
    return redirect(url_for('index'))


@app.route('/player/list')
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
    player_input = PlayerInput(name)
    db_access.add_player(player_input)
    return redirect(url_for('list_players'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if PASSWORD == request.form['password']:
            session['authorized'] = 'yes'
            if request.form['next']:
                return redirect(request.form['next'])
            return redirect(url_for('index'))
        flash('Login unsucessful', 'error')
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('authorized', None)
    return redirect(url_for('index'))
