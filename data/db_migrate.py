#!/usr/local/bin/python3
#
# Applies all new migration scripts to DB
#
import os
import sqlite3

filenames = [fn for fn in os.listdir('data/migrations') if fn.endswith('.sql')]
conn = sqlite3.connect('data/scoreboard.db')

executed_scripts = conn.execute('SELECT script FROM migration').fetchall()
ex_script_names = [r for r, in executed_scripts]

for f in sorted(filenames):
    if f not in ex_script_names:
        print(f'EXECUTING MIGRATION SCRIPT: {f}')
        sql = open(f'data/migrations/{f}').read()
        try:
            conn.executescript(sql)
            conn.execute('INSERT INTO migration VALUES (?)', (f,))
            conn.commit()
        except sqlite3.OperationalError as oe:
            print(f'Failure to execute {f}: {oe}')
            conn.rollback()
            exit(1)
    else:
        print('SKIPPING MIGRATION SCRIPT: {0}'.format(f))
