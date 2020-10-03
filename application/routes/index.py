from flask import request
from flask_restful import Resource
from application.bot.utils import BotConnection
from application.database.utils import DatabaseConnection
from application.database.models import User, Message
from application.core.utils import get_json, HTTP_STATUS_CODE
from application.core.logs import error_log


class Index(Resource):
    def post(self):
        try:
            data = get_json(request)

            new_user = User(name=data['message']['from']['first_name'],
                            is_bot=data['message']['from']['is_bot'],
                            language_code=data['message']['from']['language_code'],
                            username=data['message']['from']['username'],
                            id=data['message']['from']['id'])

            new_message = Message(id=data['message']['message_id'],
                                  date=data['message']['date'],
                                  text=data['message']['text'],
                                  user_id=data['message']['from']['id'])

            db = DatabaseConnection.get_database()

            db.session.merge(new_message)
            db.session.merge(new_user)
            db.session.commit()

            bot = BotConnection.get_telegram_bot()
            bot.send_message(data['message']['chat']['id'],
                             data['message']['text'])

        except Exception as e:
            resp = {'msg': str(e)}

            error_log('/', 'POST', str(e))
            return resp, HTTP_STATUS_CODE['BAD_REQUEST']

        return {'msg': 'ok'}, HTTP_STATUS_CODE['OK']

    def get(self):
        return 'top'
