import sqlite3


class Database:
    def __init__(self, db_name):
        # Добавьте check_same_thread=False
        self.connection = sqlite3.connect(db_name, check_same_thread=False)
        self.cursor = self.connection.cursor()

    def execute(self, query, params=None):
        if params is None:
            params = []
        self.cursor.execute(query, params)
        self.connection.commit()

    def fetchall(self, query, params=None):
        if params is None:
            params = []
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

db = Database('example.db')
