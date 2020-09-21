import requests


class TelegramBot:
    def __init__(self, token):
        self.token = token
        self.name = self._get_bot_name(token)

    def __str__(self):
        return self.name

    def send_message(self, chat_id, text):
        url = 'https://api.telegram.org/bot{}/sendMessage'.format(self.token)

        answer = self._verify_text(text)

        payload = {'chat_id': chat_id,
                   'text': answer}

        requests.post(url, json=payload)

    def _verify_text(self, text):
        try:
            number = int(text)

            if not number % 15:
                msg = 'FizzBuzz'

            elif not number % 3:
                msg = 'Fizz'

            elif not number % 5:
                msg = 'Buzz'

            else:
                msg = 'A entrada precisa ser um numero '
                msg += 'inteiro divisivel por 3, 5 ou 15'

        except Exception:
            msg = 'A entrada precisa ser um numero '
            msg += 'inteiro divisivel por 3, 5 ou 15'

        return msg

    def _get_bot_name(self, token):
        url = 'https://api.telegram.org/bot{}/getMe'.format(token)

        page = requests.get(url)

        return page.json()['result']['first_name']
