import sqlite3
from orm.my_orm.database import db


class Model:
    table_name = ''

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    @classmethod
    def create_table(cls):
        columns = ', '.join([f'{name} {col_type}' for name, col_type in cls.fields.items()])
        foreign_keys = ', '.join(cls.foreign_keys)
        query = f"CREATE TABLE IF NOT EXISTS {cls.table_name} ({columns}{', ' + foreign_keys if foreign_keys else ''})"
        db.execute(query)

    def save(self):
        fields = ', '.join(self.fields.keys())
        placeholders = ', '.join(['?'] * len(self.fields))
        values = [getattr(self, field, None) for field in self.fields]
        query = f"INSERT INTO {self.table_name} ({fields}) VALUES ({placeholders})"
        db.execute(query, values)
        self.id = db.cursor.lastrowid

    def delete(self):
        query = f"DELETE FROM {self.table_name} WHERE id = ?"
        db.execute(query, [self.id])

    @classmethod
    def all(cls):
        query = f"SELECT * FROM {cls.table_name}"
        rows = db.fetchall(query)
        return [cls(**dict(zip(cls.fields.keys(), row))) for row in rows]

    @classmethod
    def get_by_param(cls, param, value):
        query = f"SELECT * FROM {cls.table_name} WHERE {param} = ?"
        rows = db.fetchall(query, [value])
        if rows:
            return [cls(**dict(zip(cls.fields.keys(), row))) for row in rows]
        return []
