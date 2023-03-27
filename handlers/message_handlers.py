from handlers.weather_handlers import WeatherHandlers
from handlers.joke_handlers import JokeHandlers
from handlers.news_handlers import NewsHandlers
from handlers.start_handlers import StartHandlers
from handlers.echo_handlers import EchoHandlers
from handlers.stop_handlers import StopHandlers
from handlers.text_handler_answer import TextHandlerAnswer
from handlers.help_handlers import HelpHandlers


class MessageHandlers:
    def __init__(self, bot):
        self.bot = bot

        self.start_handlers = StartHandlers(bot)
        self.help_handlers = HelpHandlers(bot)
        self.echo_handlers = EchoHandlers(bot)
        self.weather_handler = WeatherHandlers(bot)
        self.news_handlers = NewsHandlers(bot)
        self.joke_handlers = JokeHandlers(bot)
        self.stop_handlers = StopHandlers(bot)
        self.text_handler_answer = TextHandlerAnswer(bot)
