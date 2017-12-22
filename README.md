# Scoreboard

A (future) ELO rating system for unscheduled matches. The guiding principles of this application are

- Simple technology for easy participation of novices -- such as [my-son](https://github.com/timothy-wilson)
- Unobtrusive functionality -- descriptive of what has happened, never prescriptive for future actions

Following is out of date in many places.

## Requirements

- Python 3.6
- Sqlite 3

## Install dependencies in virtualenvironment

Execute the following commands in PowerShell or Bash

1. `python3.6 -m venv scoreboard-venv`
1. `source scoreboard-venv/bin/activate`
1. `pip3 install -r requirements.txt`

## Running the application

    $ python scoreboard.py

Now navigate to [localhost:5000](http://localhost:5000/) to verify that it is running locally. 

## DB setup

To set up the test database, run

    $ ./init_db.py

To set up an empty database, without example data, run

    $ ./init_db.py new

## DB Migrations

When you need to make changes to the DB structure -- suppose you add a column to a table --
you will need to add a migration script to `data/migrations`. This scripts should follow a naming
convention like follows:

- `01_Example_change.sql`
- `02_Another_change.sql`

This series of scripts should allow another user to run `data/db_migrate.py` in order to transform
the test database into the structure that your changes require.

It will be common for changes to the application to require changes to the database structure.

## Useful documentation

- [Flask](http://flask.pocoo.org/docs/0.12/)
- [Jinja2](http://jinja.pocoo.org/docs/dev/)
- [Sqlite](https://sqlite.org/docs.html)
- [Python DB-API interface for SQLite](https://docs.python.org/3/library/sqlite3.html)
