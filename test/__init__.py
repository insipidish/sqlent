import sys, os
sys.path.append(os.path.join('..', 'src'))

import sqlite3 as sqlite

def create_db():
    """https://pagehalffull.wordpress.com/2013/03/05/simple-python-script-that-runs-sql-scripts-against-a-given-sqlite-database/"""
    scriptfilename = './test/Chinook_Sqlite.sql'
    dbfilename = 'test-chinook.db'

    try:
        print("\nOpening DB")
        connection = sqlite.connect(dbfilename)
        cursor = connection.cursor()

        print("Reading Script...")
        scriptFile = open(scriptfilename, 'r')
        script = scriptFile.read()
        scriptFile.close()

        print("Running Script...")
        cursor.executescript(script)

        connection.commit()
        print("Changes successfully committed\n")

    except Exception as e:
        print("Something went wrong:")
        print (e)
    finally:
        print("\nClosing DB")
        connection.close()


def setup():
    create_db()
