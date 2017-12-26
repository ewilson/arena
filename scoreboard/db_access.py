from collections import namedtuple
import sqlite3

from flask import g

from . import util

MatchOutput = namedtuple(
    'Match',
    ['id', 'winner_name', 'winner_score', 'loser_name', 'loser_score', 'datetime_added']
)
PlayerOutput = namedtuple(
    'Player', ['id', 'name']
)


def add_match(match_input):
    conn = get_db()
    cur = conn.cursor()
    cur.execute('INSERT INTO match (datetime_added) values (:datetime_added)',
                 {'datetime_added': match_input.datetime_added})
    match_id = cur.lastrowid
    match_player_insert = '''
    INSERT INTO match_player (match_id, player_id, score, opponent_score, win)
    values (:match_id, :player_id, :score, :opponent_score, :win)'''
    cur.execute(match_player_insert,
    {
        'match_id': match_id,
        'player_id': match_input.winner_id,
        'score': match_input.winner_score,
        'opponent_score': match_input.loser_score,
        'win': True
    })
    cur.execute(match_player_insert, {
        'match_id': match_id,
        'player_id': match_input.loser_id,
        'score': match_input.loser_score,
        'opponent_score': match_input.winner_score,
        'win': False
    })
    conn.commit()
    return match_id


def get_matches():
    conn = get_db()
    match_select = '''
    SELECT 
        m.id id,
        m.datetime_added datetime_added,
        wp.name winner_name, 
        wmp.score winner_score,
        lp.name loser_name,
        lmp.score loser_score
    FROM match m, match_player wmp, match_player lmp, player wp, player lp
    WHERE m.id = wmp.match_id
    AND m.id = lmp.match_id
    AND wmp.player_id = wp.id
    AND lmp.player_id = lp.id
    AND wmp.win = 1
    AND lmp.win = 0
    ORDER BY m.datetime_added DESC
    '''
    results = conn.execute(match_select)
    return [util.row_to_namedtuple(MatchOutput, r) for r in results]


def get_players():
    conn = get_db()
    results = conn.execute('SELECT id, name FROM player ORDER BY name').fetchall()
    return [util.row_to_namedtuple(PlayerOutput, r) for r in results]


def delete_player(player_id):
    conn = get_db()
    conn.execute('DELETE FROM player WHERE id = :id', {'id': player_id})
    conn.commit()


def add_player(player_input):
    conn = get_db()
    cur = conn.cursor()
    cur.execute('INSERT INTO player (name) values (:name)',
                 {'name': player_input.name})
    player_id = cur.lastrowid
    conn.commit()
    return player_id


def get_db():
    if not hasattr(g, 'scoreboard.db'):
        g.conn = connect_db()
    return g.conn


def connect_db():
    conn = sqlite3.connect('data/scoreboard.db')
    conn.row_factory = sqlite3.Row
    return conn
