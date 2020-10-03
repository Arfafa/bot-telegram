from application.database.utils import DatabaseConnection

db = DatabaseConnection.get_database()


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    is_bot = db.Column(db.Boolean)
    language_code = db.Column(db.Text)
    username = db.Column(db.Text)


class Message(db.Model):
    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Integer)
    text = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
