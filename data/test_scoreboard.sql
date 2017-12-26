-- GENERATED SQL DUMP -- DO NOT MODIFY -- WILL BE OVERWRITTEN
PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE player (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);
INSERT INTO "player" VALUES(1,'Eli');
INSERT INTO "player" VALUES(2,'Simon');
INSERT INTO "player" VALUES(3,'Tim');
INSERT INTO "player" VALUES(4,'Nathan');
CREATE TABLE migration (
    script TEXT PRIMARY KEY
);
INSERT INTO "migration" VALUES('01_Add_match_table.sql');
CREATE TABLE match (
    id INTEGER PRIMARY KEY,
    datetime_added TEXT NOT NULL
);
INSERT INTO "match" VALUES(1,'2017-12-26 18:30:38');
INSERT INTO "match" VALUES(2,'2017-12-26 18:31:01');
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
INSERT INTO "match_player" VALUES(1,2,21,15,1);
INSERT INTO "match_player" VALUES(1,1,15,21,0);
INSERT INTO "match_player" VALUES(2,4,43,41,1);
INSERT INTO "match_player" VALUES(2,3,41,43,0);
COMMIT;
