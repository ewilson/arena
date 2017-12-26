CREATE TABLE match (
    id INTEGER PRIMARY KEY,
    datetime_added TEXT NOT NULL
);

CREATE TABLE match_player (
    match_id INTEGER NOT NULL,
    player_id INTEGER NOT NULL,
    score INTEGER NOT NULL,
    opponent_score INTEGER NOT NULL,
    win BOOLEAN NOT NULL,
    PRIMARY KEY (match_id, player_id),
    FOREIGN KEY (match_id) REFERENCES match(id),
    FOREIGN KEY (player_id) REFERENCES player(id)
);
