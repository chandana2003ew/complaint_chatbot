import sqlite3

def get_db():
    conn = sqlite3.connect('complaints.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with open('database/schema.sql') as f:
        get_db().executescript(f.read())
