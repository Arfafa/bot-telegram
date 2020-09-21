from application.database.database import Database

DATABASE = Database('banco.db')


def get_database():
    return DATABASE
