import sqlite3, unittest
from .helpers import get_sql_results
from ..sqlent.query import Query
from ..test import db_path

conn = None

def setup_module(module):
    global conn
    print ("") # this is to get a newline after the dots
    print ("getting connection")
    conn = sqlite3.connect(db_path)

def teardown_module(module):
    print ("closing connection")
    conn.close()

def test_select_all():
    results = get_sql_results(conn, Query().select().table('Artist').to_string())
    assert(len(results)==275)
    assert('Jimi' in results[93][1])


class TestSelectWhereEquality(unittest.TestCase):
    def test_multiple_equality_no_result(self):
        query = Query().select().table('Artist').where('ArtistId', 1)
        query = query.where('Name', 'Jimi')
        results = get_sql_results(conn, query.to_string())
        self.assertEqual(len(results),0)

    def test_multiple_equality_with_result(self):
        query = Query().select().table('Artist').where('ArtistId', 1)
        query = query.where('Name', 'AC/DC')
        results = get_sql_results(conn, query.to_string())
        self.assertEqual(len(results),1)
        self.assertTrue('AC/DC' in results[0][1])

class TestSelectWhereIndividually(unittest.TestCase):
    def test_equality(self):
        results = get_sql_results(conn, Query().select().table('Artist').where('ArtistId', 1).to_string())
        self.assertEqual(len(results),1)
        self.assertTrue('AC/DC' in results[0][1])

    def test_less(self):
        query = Query().select().table('Artist').where('ArtistId', '<', 2)
        results = get_sql_results(conn, query.to_string())
        self.assertEqual(len(results),1)
        self.assertTrue('AC/DC' in results[0][1])

    def test_greater(self):
        query = Query().select().table('Artist').where('ArtistId', '>', 274)
        results = get_sql_results(conn, query.to_string())
        self.assertEqual(len(results),1)
        self.assertTrue('Philip' in results[0][1])

    def test_not_in(self):
        query = Query().select().table('Artist').where_not('Name', 'in', ['AC/DC', 'Jimi Hendrix'])
        print(query.to_string())
        results = get_sql_results(conn, query.to_string())
        self.assertTrue('AC/DC' not in [row[1] for row in results])
        self.assertTrue('Jimi' not in [row[1] for row in results])
