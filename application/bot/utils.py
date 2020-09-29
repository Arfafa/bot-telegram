import os
from application.bot.telegram_bot import TelegramBot


class BotConnection:
    _telegram_token = os.environ.get('TELEGRAM_TOKEN', '')
    _telegram_bot = None

    @classmethod
    def get_telegram_bot(cls):
        if cls._telegram_bot is None:
            cls._telegram_bot = TelegramBot(cls._telegram_token)

        return cls._telegram_bot
