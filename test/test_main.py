from ..test import db_path
import sqlite3
conn = None

def setup_module(module):
    global conn
    print ("") # this is to get a newline after the dots
    print ("getting connection")
    conn = sqlite3.connect(db_path)

def teardown_module(module):
    print ("closing connection")
    conn.close()

def test_db_setup():
    cur = conn.cursor()
    cur.execute("select * from Artist")
    results = cur.fetchall()
    cur.close()
    assert(len(results)==275)
    assert('Jimi' in results[93][1])
