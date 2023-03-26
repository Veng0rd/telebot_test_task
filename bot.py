import telebot
from handlers.message_handlers import MessageHandlers


class TelegramBot:
    def __init__(self, token):
        self.bot = telebot.TeleBot(token, skip_pending=True)
        self.message_handlers = MessageHandlers(self.bot)

    def run(self):
        self.bot.polling(non_stop=True, skip_pending=True)
