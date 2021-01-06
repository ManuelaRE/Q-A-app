from flask import g
import sqlite3
import psycopg2
from psycopg2.extras import DictCursor

# DATABASE = 'questions.db'
# # connect to the database
# def connect_db():
#     sql = sqlite3.connect(DATABASE)
#     sql.row_factory = sqlite3.Row
#     return sql

# # get the database when I need
# def get_db():
#     if not hasattr(g, 'sqlite3'):
#         g.sqlite_db = connect_db()
#     return g.sqlite_db  


def connect_db():
    conn = psycopg2.connect('postgres://hzsirizlagwamf:3a5134e704da98fcaee12f52ff26a28d77c546fc2de1290c861868a7b016abe6@ec2-52-87-135-240.compute-1.amazonaws.com:5432/dfrraf49sf1dqr', cursor_factory=DictCursor)
    conn.autocommit = True
    sql = conn.cursor()
    return conn, sql

def get_db():
    db = connect_db()

    if not hasattr(g, 'postgres_db_conn'):
        g.postgres_db_conn = db[0]

    if not hasattr(g, 'postgres_db_cur'):
        g.postgres_db_cur = db[1]

    return g.postgres_db_cur

def init_db():
    db = connect_db()

    db[1].execute(open('schema.sql', 'r').read())
    db[1].close()

    db[0].close()

def init_admin():
    db = connect_db()

    db[1].execute('update users set admin = True where name = %s', ('admin', ))

    db[1].close()
    db[0].close()

def init_admin():
    db = connect_db()
    
    db[1].execute('update usersfile set admin = True where name = %s', ('admin', ))   
    db[1].close() 
    db[0].close()