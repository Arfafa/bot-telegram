import os


class Config:
    DEBUG = False
    JSONIFY_PRETTYPRINT_REGULAR = True
    RESTFUL_JSON = {'ensure_ascii': False}
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL',
                                             'sqlite:///default.db')


class DebugConfig(Config):
    DEBUG = True
