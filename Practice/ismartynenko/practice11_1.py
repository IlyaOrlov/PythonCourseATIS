import sqlite3
import json


class SqlWrapper:
    def __enter__(self):
        _db_name = "films.db"
        self.conn = sqlite3.connect(_db_name)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()

    def select(self, query):
        cur = self.conn.cursor()
        cur.execute(query)
        print(json.dumps(cur.fetchall()))

    def execute(self, query):
        cur = self.conn.cursor()
        cur.execute(query)
        self.conn.commit()


if __name__ == "__main__":
    with SqlWrapper() as sqw:
        sqw.execute("INSERT INTO films (name, desc) VALUES ('Cool Film', 'SHORT LONG STORY')")
        sqw.select("SELECT * FROM films")
        sqw.execute("INSERT INTO films (name, desc) VALUES ('UnCool Film', 'unSHORT LONG STORY')")
        sqw.select("SELECT * FROM films WHERE name = 'UnCool Film'")

