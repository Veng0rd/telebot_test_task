class TextHandlerAnswer:
    def __init__(self, bot):
        self.bot = bot

        @self.bot.message_handler(func=lambda message: True)
        def text_handler_answer(message):
            chat_id = message.chat.id
            '''Сообщение об незарегистрированном сообщении/команде'''
            self.bot.send_message(chat_id,
                                  'Я работаю только по запрограммированным командам, введите <i><b>/help</b></i> '
                                  'для просмотра доступных команд',
                                  parse_mode='html')
