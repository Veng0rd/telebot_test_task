class StopHandlers:
    def __init__(self, bot):
        self.bot = bot

        @self.bot.message_handler(commands=['stop'])
        def stop_handlers(message):
            chat_id = message.chat.id
            """Прощание и остановка бота"""
            self.bot.send_message(chat_id, 'Я завершаю свою работу.\n'
                                           'До скорых встреч!', parse_mode='html')
            self.bot.stop_polling()
