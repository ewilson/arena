import sqlite3

from flask import g

def get_players():
    conn = get_db()
    return conn.execute('SELECT id, name FROM player').fetchall()


def delete_player(player_id):
    conn = get_db()
    conn.execute('DELETE FROM player WHERE id = :id', {'id': player_id})
    conn.commit()


def add_player(name):
    conn = get_db()
    conn.execute('INSERT INTO player (name) values (:name)',
                 {'name': name})
    conn.commit()


def get_db():
    if not hasattr(g, 'scoreboard.db'):
        g.conn = connect_db()
    return g.conn


def connect_db():
    conn = sqlite3.connect('data/scoreboard.db')
    conn.row_factory = sqlite3.Row
    return conn
