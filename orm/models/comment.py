from orm.my_orm.model import Model


class Comment(Model):
    table_name = 'comments'
    fields = {
        'id': 'INTEGER PRIMARY KEY AUTOINCREMENT',
        'text': 'TEXT',
        'user_id': 'INTEGER',
        'article_id': 'INTEGER'
    }
    foreign_keys = [
        'FOREIGN KEY(user_id) REFERENCES users(id)',
        'FOREIGN KEY(article_id) REFERENCES articles(id)'
    ]


Comment.create_table()
