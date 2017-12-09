#!/bin/bash
#
# Run this step to save the state of the test database
#
TEST_DB_NAME='data/test_arena.sql'

rm $TEST_DB_NAME
echo '-- GENERATED SQL DUMP -- DO NOT MODIFY -- WILL BE OVERWRITTEN' > $TEST_DB_NAME
sqlite3 data/arena.db .dump >> $TEST_DB_NAME
