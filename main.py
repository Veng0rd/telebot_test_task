import bot
from config.config import TOKEN

if __name__ == '__main__':
    telebot = bot.TelegramBot(TOKEN)
    telebot.run()
