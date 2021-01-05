from flask import g
import sqlite3


DATABASE = 'questions.db'
# connect to the database
def connect_db():
    sql = sqlite3.connect(DATABASE)
    sql.row_factory = sqlite3.Row
    return sql

# get the database when I need
def get_db():
    if not hasattr(g, 'sqlite3'):
        g.sqlite_db = connect_db()
    return g.sqlite_db  