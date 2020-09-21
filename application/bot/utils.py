import os
from application.bot.telegram_bot import TelegramBot

TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN', '')
TELEGRAM_BOT = TelegramBot(TELEGRAM_TOKEN)


def get_telegram_bot():
    return TELEGRAM_BOT
