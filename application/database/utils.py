from flask_sqlalchemy import SQLAlchemy


class DatabaseConnection:
    _database = None

    @classmethod
    def get_database(cls):
        if cls._database is None:
            cls._database = SQLAlchemy()

        return cls._database
