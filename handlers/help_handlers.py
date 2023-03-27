from util import print_commands


class HelpHandlers:
    def __init__(self, bot):
        self.bot = bot

        @self.bot.message_handler(commands=['help'])
        def help_handlers(message):
            chat_id = message.chat.id
            """Вывод списка доступных команд при команде /help"""
            self.bot.send_message(chat_id, print_commands(), parse_mode='html')
