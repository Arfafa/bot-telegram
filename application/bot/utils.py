from application.bot.telegram_bot import TelegramBot

TELEGRAM_TOKEN = '484342312:AAEVje5CZ_ZQ5UgJtWsrtunBoH7yhzdoy2w'
TELEGRAM_BOT = TelegramBot(TELEGRAM_TOKEN)


def get_telegram_bot():
    return TELEGRAM_BOT
