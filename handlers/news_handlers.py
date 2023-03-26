import random
from newsapi import NewsApiClient
from config.config import NEWS_API_KEY


class NewsHandlers:
    def __init__(self, bot):
        self.bot = bot

        @self.bot.message_handler(commands=['news'])
        def news_handlers(message):
            chat_id = message.chat.id
            """Сообщение для PyCharm, что я знаю, что это исключение слишком большое и я с этим согласен"""
            # noinspection PyBroadException
            try:
                newsapi = NewsApiClient(api_key=NEWS_API_KEY)
                news_top_headlines = newsapi.get_top_headlines(language='ru')['articles']
                news_list = [source['title'] for source in news_top_headlines]
                self.bot.send_message(chat_id, random.choice(news_list), parse_mode='html')
            except Exception:
                self.bot.send_message(chat_id, 'Не удалось получить последние новости', parse_mode='html')
