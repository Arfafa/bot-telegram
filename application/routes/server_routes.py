from flask import request
from flask_restful import Resource
from application.server import api
from application.bot.utils import get_telegram_bot
from application.database.utils import get_database
from application.routes.utils import get_json
from application.routes.utils import HTTP_STATUS_CODE
from application.routes.logs import error_log


class Index(Resource):
    def post(self):
        try:
            data = get_json(request)

            database = get_database()
            database.insert_information(data)

            bot = get_telegram_bot()
            bot.send_message(data['message']['chat']['id'],
                             data['message']['text'])

        except Exception as e:
            resp = {'msg': str(e)}

            error_log('/', 'POST', str(e))

            return resp, HTTP_STATUS_CODE['BAD_REQUEST']

        return {'msg': 'ok'}, HTTP_STATUS_CODE['OK']

    def get(self):
        return 'top'


def init_routes():
    api.add_resource(Index, '/')
