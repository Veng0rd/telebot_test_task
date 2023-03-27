from config.config import commands
from telebot import util


def print_commands():
    list_of_commands = 'Список моих команд:\n\n'
    for element in commands:
        list_of_commands += f'<b>{element[0]}</b>   <i>{element[1]}</i>\n\n'
    return list_of_commands


def get_echo_text(echo_text):
    return util.extract_arguments(echo_text)
