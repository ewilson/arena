import sqlite3

from flask import app, g

from arena import app

def get_all_chirps():
    conn = get_db()
    return conn.execute('''
        SELECT c.id, c.body, c.datetime, u.handle
        FROM chirp c, user u
        WHERE c.user_id = u.id
    ''').fetchall()


def delete_chirp(chirp_id):
    conn = get_db()
    conn.execute('DELETE FROM chirp WHERE id = :id', {'id': chirp_id})
    conn.commit()


def get_all_users():
    conn = get_db()
    return conn.execute('SELECT id, handle, admin FROM user').fetchall()


def delete_user(user_id):
    conn = get_db()
    conn.execute('DELETE FROM user WHERE id = :id', {'id': user_id})
    conn.commit()


def add_user(handle):
    conn = get_db()
    conn.execute('INSERT INTO user (handle, admin) values (:handle, :admin)',
                 {'handle': handle, 'admin': 0})
    conn.commit()


def get_db():
    if not hasattr(g, 'arena.db'):
        g.conn = connect_db()
    return g.conn


def connect_db():
    conn = sqlite3.connect('data/arena.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'conn'):
        g.conn.close()
