import requests
from config.settings import TELEGRAM_URL_BOT, TELEGRAM_TOKEN, TELEGRAM_USER_ID


class MyBot:
    """
    Класс для отправки сообщения через бот телеграм.
    """
    URL = TELEGRAM_URL_BOT
    TOKEN = TELEGRAM_TOKEN
    MY_ID = TELEGRAM_USER_ID

    def send_message(self, text):
        requests.post(
            url=f'{self.URL}{self.TOKEN}/sendMessage',
            data={
                'chat_id': self.MY_ID,
                'text': text
            }
        )