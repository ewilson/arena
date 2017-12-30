from collections import namedtuple
from datetime import datetime

MatchInput = namedtuple(
    'Match',
    'winner_id,winner_score,loser_id,loser_score,datetime_added'
)


def get_formatted_datetime():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def build_match(params):
    player1_id = params['player1']
    player2_id = params['player2']
    score1 = params['score1']
    score2 = params['score2']
    print(params)
    winner_id, loser_id = (player1_id, player2_id) if score1 > score2 else (player2_id, player1_id)
    win_score, lose_score = max(score1, score2), min(score1, score2)
    datetime_added = get_formatted_datetime()
    return MatchInput(winner_id, win_score, loser_id, lose_score, datetime_added)
