from flask import Flask, request, g, render_template, redirect, url_for

import db_access

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/player/list')
def list_players():
    players = db_access.get_players()
    return render_template('player/list.html', players=players)


@app.route('/player/delete/<player_id>')
def delete_player(player_id):
    db_access.delete_player(player_id)
    return redirect(url_for('list_players'))


@app.route('/player/add', methods=['POST'])
def add_player():
    name = request.form.get('name')
    db_access.add_player(name)
    return redirect(url_for('list_players'))


if __name__ == '__main__':
    app.run(debug=True)
