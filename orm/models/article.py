from orm.my_orm.model import Model


class Article(Model):
    table_name = 'articles'
    fields = {
        'id': 'INTEGER PRIMARY KEY AUTOINCREMENT',
        'title': 'TEXT',
        'text': 'TEXT',
        'user_id': 'INTEGER'
    }
    foreign_keys = [
        'FOREIGN KEY(user_id) REFERENCES users(id)'
    ]


Article.create_table()
