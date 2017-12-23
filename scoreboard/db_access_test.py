import os
import sqlite3

import pytest

from scoreboard import db_access

TEST_DB_NAME = 'data/test_scoreboard.db'
SCHEMA_FILE = 'data/test_scoreboard.sql'


@pytest.fixture
def test_get_db():
    if os.path.isfile(TEST_DB_NAME):
        os.remove(TEST_DB_NAME)
    conn = sqlite3.connect(TEST_DB_NAME)
    schema = open(SCHEMA_FILE).read()
    conn.executescript(schema)
    conn.commit()

    def connect_test_db():
        conn = sqlite3.connect(TEST_DB_NAME)
        conn.row_factory = sqlite3.Row
        return conn

    return connect_test_db


def test_get_players(monkeypatch, test_get_db):
    monkeypatch.setattr(db_access, 'get_db', test_get_db)

    players = db_access.get_players()

    assert len(players) == 4
    assert players[1]['name'] == 'Tim'


def test_add_player(monkeypatch, test_get_db):
    monkeypatch.setattr(db_access, 'get_db', test_get_db)

    orig_player_num = len(db_access.get_players())

    db_access.add_player('Charles')

    current_players = db_access.get_players()

    print(current_players)
    assert current_players[orig_player_num]['name'] == 'Charles'


def test_delete_player(monkeypatch, test_get_db):
    monkeypatch.setattr(db_access, 'get_db', test_get_db)

    orig_players = db_access.get_players()
    tim, = [p for p in orig_players if p['name'] == 'Tim']

    db_access.delete_player(tim['id'])

    current_players = db_access.get_players()

    assert not [p for p in current_players if p['name'] == 'Tim']
    assert len(current_players) == len(orig_players) - 1
