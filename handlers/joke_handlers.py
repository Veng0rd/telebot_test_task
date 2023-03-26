import pyjokes
from easygoogletranslate import EasyGoogleTranslate


class JokeHandlers:
    def __init__(self, bot):
        self.bot = bot

        @self.bot.message_handler(commands=['joke'])
        def joke_handlers(message):
            chat_id = message.chat.id
            """Сообщение для PyCharm, что я знаю, что это исключение слишком большое и я с этим согласен"""
            # noinspection PyBroadException
            try:
                translator = EasyGoogleTranslate()
                self.bot.send_message(chat_id, translator.translate(pyjokes.get_joke(), target_language='ru'),
                                      parse_mode='html')
            except Exception:
                self.bot.send_message(chat_id, 'Не удалось найти шутку', parse_mode='html')
