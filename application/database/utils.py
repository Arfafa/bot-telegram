from application.database.database import Database


class DatabaseConnection:
    _database = None

    @classmethod
    def get_database(cls):
        if cls._database is None:
            cls._database = Database('banco.db')

        return cls._database
