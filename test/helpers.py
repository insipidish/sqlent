def get_sql_results(conn, sql):
    cur = conn.cursor()
    cur.execute(sql)
    results = cur.fetchall()
    cur.close()
    return results
