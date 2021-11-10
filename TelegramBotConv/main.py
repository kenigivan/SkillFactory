import telebot
from telebot import types
from extensions import APIException, Converter
from config import *


def create_markup(base = None):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    button = []
    for val in exchanges.keys():
        if val != base:
            button.append(types.KeyboardButton(val.capitalize()))

    markup.add(*button)
    return markup


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def start(message: telebot.types.Message):
    text = "Здравтвуйте!\nДля начала конвертации валюты наберите\nкоманду: /convert\n(или нажмите на неё)"
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for i in exchanges.keys():
        text = '\n'.join((text, i))
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['convert'])
def values(message: telebot.types.Message):
    text = 'Выберите ваюту, из которой конвертировать:'
    bot.send_message(message.chat.id, text, reply_markup=create_markup())
    bot.register_next_step_handler(message, base_handler)


def base_handler(message: telebot.types.Message):
    base = message.text.strip().lower()
    text = 'Выберите ваюту, в которую конвертировать:'
    bot.send_message(message.chat.id, text, reply_markup=create_markup(base))
    bot.register_next_step_handler(message, sym_handler, base)


def sym_handler(message: telebot.types.Message, base):
    sym = message.text.strip().lower()
    text = 'Введите количество конвертируемой валюты:'
    bot.send_message(message.chat.id, text)
    bot.register_next_step_handler(message, amount_handler, base, sym)


def amount_handler(message: telebot.types.Message, base, sym):
    amount = message.text.strip()
    try:
        new_price = Converter.get_price(base, sym, amount)
    except APIException as e:
        bot.send_message(message.chat.id, f"Ошибка конвертации:\n{e}")
    else:
        text = f"Цена {amount} {base} в {sym} : {new_price}"
        bot.send_message(message.chat.id, text)


bot.polling()
