from unittest import mock as mock

from . import match_service


def test_build_match(monkeypatch):
    monkeypatch.setattr(match_service, 'get_formatted_datetime', mock.Mock(return_value='2018-01-01'))
    player1_id, player2_id = mock.Mock(), mock.Mock()
    score1, score2 = 5, 11

    result = match_service.build_match({
        'player1': player1_id,
        'player2': player2_id,
        'score1': score1,
        'score2': score2
    })

    assert result.winner_id == player2_id
    assert result.winner_score == 11
    assert result.loser_id == player1_id
    assert result.loser_score == 5
    assert result.datetime_added == '2018-01-01'
