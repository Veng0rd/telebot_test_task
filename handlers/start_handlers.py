from config.config import commands
from util import print_commands
from telebot import types


class StartHandlers:
    def __init__(self, bot):
        self.bot = bot

        @self.bot.message_handler(commands=['start'])
        def start_handlers(message):
            chat_id = message.chat.id
            username = message.from_user.first_name  # получение имени пользователя
            self.bot.send_message(chat_id, f'Привет <i><b>{username}</b></i>!', parse_mode='html')
            """Отправка списка команд в чат"""
            self.bot.send_message(chat_id, print_commands(), parse_mode='html')
            """Регистрация команд в меню"""
            self.bot.set_my_commands(types.BotCommand(command[0], command[1]) for command in commands)
