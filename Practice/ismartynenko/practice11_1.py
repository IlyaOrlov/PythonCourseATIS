import sqlite3
import json


class SqlWrapper:
    def __init__(self, dbname):
        self.db_name = dbname

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()

    def select(self, query):
        cur = self.conn.cursor()
        cur.execute(query)
        return json.dumps(cur.fetchall())

    def execute(self, query):
        cur = self.conn.cursor()
        cur.execute(query)
        self.conn.commit()


if __name__ == "__main__":
    with SqlWrapper("films.db") as sqw:
        sqw.execute("INSERT INTO films (name, desc) VALUES ('Cool Film', 'SHORT LONG STORY')")
        q1 = sqw.select("SELECT * FROM films")
        print(q1)
        sqw.execute("INSERT INTO films (name, desc) VALUES ('UnCool Film', 'unSHORT LONG STORY')")
        print(sqw.select("SELECT * FROM films WHERE name = 'UnCool Film'"))
