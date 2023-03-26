from telebot import types, util
from config.config import commands
from handlers.weather_handlers import WeatherHandlers
from handlers.joke_handlers import JokeHandlers
from handlers.news_handlers import NewsHandlers


class MessageHandlers:
    def __init__(self, bot):
        self.bot = bot
        self.weather_handler = WeatherHandlers(bot)
        self.joke_handlers = JokeHandlers(bot)
        self.news_handlers = NewsHandlers(bot)

        @self.bot.message_handler(commands=['start'])
        def start_handlers(message):
            chat_id = message.chat.id
            username = message.from_user.first_name  # получение имени пользователя
            self.bot.send_message(chat_id, f'Привет <i><b>{username}</b></i>!', parse_mode='html')
            print_commands(chat_id)
            """Регистрация команд в меню"""
            self.bot.set_my_commands(types.BotCommand(command[0], command[1]) for command in commands)

        @self.bot.message_handler(commands=['help'])
        def help_handlers(message):
            chat_id = message.chat.id
            """Вывод списка доступных команд при команде /help"""
            print_commands(chat_id)

        @self.bot.message_handler(commands=['echo'])
        def echo_handlers(message):
            chat_id = message.chat.id
            """Получает текст сообщения после /echo"""
            echo_text = util.extract_arguments(message.text)
            if echo_text != '':
                self.bot.send_message(chat_id, echo_text, parse_mode='html')
            else:
                self.bot.send_message(chat_id, 'Чтобы получить эхо-ответ, после команды /echo <b>добавьте текст'
                                               ' для ответа</b>.\n\n'
                                               'Например: /echo <i>это мой текст для эхо-ответа</i>',
                                      parse_mode='html')

        @self.bot.message_handler(commands=['stop'])
        def stop_handlers(message):
            chat_id = message.chat.id
            """Прощание и остановка бота"""
            self.bot.send_message(chat_id, 'Я завершаю свою работу.\n'
                                           'До скорых встреч!', parse_mode='html')
            self.bot.stop_polling()

        @self.bot.message_handler(content_types=['text'])
        def text_handler(message):
            chat_id = message.chat.id
            '''Сообщение об незарегистрированном сообщении/команде'''
            self.bot.send_message(chat_id,
                                  'Я работаю только по запрограммированным командам, введите <i><b>/help</b></i> '
                                  'для просмотра доступных команд',
                                  parse_mode='html')

        def print_commands(chat_id):
            list_of_commands = 'Список моих команд:\n\n'
            for element in commands:
                list_of_commands += f'<b>{element[0]}</b>   <i>{element[1]}</i>\n\n'
            self.bot.send_message(chat_id, list_of_commands, parse_mode='html')
