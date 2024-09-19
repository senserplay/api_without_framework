import sqlite3


class Database:
    def __init__(self, db_name):
        # Добавляем check_same_thread=False для потокобезопасности
        self.connection = sqlite3.connect(db_name, check_same_thread=False)
        self.connection.execute("PRAGMA foreign_keys = ON")
        self.connection.commit()

    def execute(self, query, params=None):
        if params is None:
            params = []
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        self.connection.commit()
        return cursor  # Возвращаем курсор для получения lastrowid

    def fetchall(self, query, params=None):
        if params is None:
            params = []
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        return cursor.fetchall()


db = Database('example.db')
