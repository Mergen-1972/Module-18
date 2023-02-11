import requests
import telebot
from telebot import types

from Extensions import ConvertionException , CurrencyChanger
from Config import keys,TOKEN

bot=telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start''help'])
def help(message: telebot.types.Message):


    text = 'Чтобы начать работу введите команду боту в формате:\n<имя валюты>\
<в какую валюту перевести>\
<количество переводимой валюты>'
    bot.reply_to(message , text)

@bot.message_handler(commands=['values'])
def value(message: telebot.types.Message):

    text = 'Доступные валюты'
    for key in keys.keys():
        text = '\n'.join((text, key))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):


    values = message.text.split()

    quote, base, amount = values
    total_base = CurrencyChanger(quote, base, amount)
    bot.send_message(message.chat.id, 'text')

    text: str = f'цена{amount} {quote}в{base}-{total_base}'



bot.polling(none_stop=True)