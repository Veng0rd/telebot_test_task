from util import get_echo_text


class EchoHandlers:
    def __init__(self, bot):
        self.bot = bot

        @self.bot.message_handler(commands=['echo'])
        def echo_handlers(message):
            chat_id = message.chat.id
            """Получает текст сообщения после /echo"""
            echo_text = get_echo_text(message.text)
            if echo_text != "":
                self.bot.send_message(chat_id, echo_text, parse_mode='html')
            else:
                self.bot.send_message(chat_id, 'Чтобы получить эхо-ответ, после команды /echo <b>добавьте текст'
                                               ' для ответа</b>.\n\n'
                                               'Например: /echo <i>это мой текст для эхо-ответа</i>',
                                      parse_mode='html')
