import os
import sqlite3
import unittest.mock as mock

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


def test_get_matches(monkeypatch, test_get_db):
    monkeypatch.setattr(db_access, 'get_db', test_get_db)

    matches = db_access.get_matches()

    assert len(matches) == 2
    assert matches[0].winner_name == 'Nathan'
    assert matches[0].loser_name == 'Tim'
    assert matches[0].winner_score == 43
    assert matches[0].loser_score == 41
    assert matches[0].datetime_added.startswith('2017-12-27')


def test_add_match(monkeypatch, test_get_db):
    monkeypatch.setattr(db_access, 'get_db', test_get_db)
    match_input = mock.Mock(
        winner_id=1, winner_score=21,
        loser_id=2, loser_score=17,
        datetime_added='2018-01-01'
    )

    match_id = db_access.add_match(match_input)

    matches = db_access.get_matches()

    added_match, = [m for m in matches if m.id == match_id]
    assert added_match.winner_name == 'Eli'
    assert added_match.loser_name == 'Simon'
    assert added_match.winner_score == 21
    assert added_match.loser_score == 17
    assert added_match.datetime_added == '2018-01-01'


def test_get_players(monkeypatch, test_get_db):
    monkeypatch.setattr(db_access, 'get_db', test_get_db)

    players = db_access.get_players()

    assert len(players) == 4
    # should be alphabetical
    assert 'ENST' == ''.join([p.name[0] for p in players])


def test_add_player(monkeypatch, test_get_db):
    player_input = mock.Mock()
    player_input.name = 'Charles'
    monkeypatch.setattr(db_access, 'get_db', test_get_db)

    charles_id = db_access.add_player(player_input)

    charles, = [p for p in db_access.get_players() if p.id == charles_id]

    assert charles.name == 'Charles'


def test_delete_player(monkeypatch, test_get_db):
    monkeypatch.setattr(db_access, 'get_db', test_get_db)

    orig_players = db_access.get_players()
    tim, = [p for p in orig_players if p.name == 'Tim']

    db_access.delete_player(tim.id)

    current_players = db_access.get_players()

    assert not [p for p in current_players if p.name == 'Tim']
    assert len(current_players) == len(orig_players) - 1
