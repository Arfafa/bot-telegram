from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from application.routes.index import Index
from application.database.utils import DatabaseConnection


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object('config.Config')

    api = Api(app)
    api.add_resource(Index, '/')

    db = DatabaseConnection.get_database()
    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app
