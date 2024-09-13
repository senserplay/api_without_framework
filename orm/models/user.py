from orm.my_orm.model import Model


class User(Model):
    table_name = 'users'
    fields = {
        'id': 'INTEGER PRIMARY KEY AUTOINCREMENT',
        'name': 'TEXT',
        'email': 'TEXT',
        'login': 'TEXT',
        'password': 'TEXT'
    }


User.create_table()
