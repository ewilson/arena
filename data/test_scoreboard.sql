-- GENERATED SQL DUMP -- DO NOT MODIFY -- WILL BE OVERWRITTEN
PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE player (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);
INSERT INTO "player" VALUES(1,'Eli');
INSERT INTO "player" VALUES(2,'Tim');
INSERT INTO "player" VALUES(3,'Simon');
INSERT INTO "player" VALUES(4,'Nathan');
CREATE TABLE migration (
    script TEXT PRIMARY KEY
);
COMMIT;
