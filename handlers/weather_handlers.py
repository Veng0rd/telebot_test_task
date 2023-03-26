import requests
from config.config import OPEN_WEATHER_TOKEN
from telebot import util


class WeatherHandlers:
    def __init__(self, bot):
        self.bot = bot

        @self.bot.message_handler(commands=['weather'])
        def weather_handlers(message):
            chat_id = message.chat.id
            city = util.extract_arguments(message.text)
            if city != '':
                try:
                    res = requests.get(
                        f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPEN_WEATHER_TOKEN}',
                        params={'units': 'metric', 'lang': 'ru'})
                    data = res.json()
                    self.bot.send_message(chat_id, f'В городе {data["name"]} сегодня '
                                                   f'<b>{data["weather"][0]["description"]}</b>\n'
                                                   f'Температура составляет <b>{data["main"]["temp"]}°C</b>\n'
                                                   f'Макс.: <b>{data["main"]["temp_max"]}</b>°C, '
                                                   f'мин.: <b>{data["main"]["temp_min"]}°C</b>\n'
                                                   f'Ощущается как <b>{data["main"]["feels_like"]}°C</b>\n'
                                                   f'Влажность - <b>{data["main"]["humidity"]} %</b>\n'
                                                   f'Скорость ветра - <b>{data["wind"]["speed"]} м/с</b>',
                                          parse_mode='html')
                except KeyError:
                    self.bot.send_message(chat_id, 'Не удалось получить данные о погоде в указанном городе')
            else:
                self.bot.send_message(chat_id,
                                      'Чтобы получить текущую погоду в указанном городе, после команды /weather <b>'
                                      'добавьте название интересующего вас города</b>.\n\nНапример:'
                                      ' /weather <i>Омск</i>', parse_mode='html')
