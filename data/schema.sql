-- Original schema, do not modify. Changes will be added in migrations
CREATE TABLE app_user (
    id INTEGER PRIMARY KEY,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE player (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE migration (
    script TEXT PRIMARY KEY
);
