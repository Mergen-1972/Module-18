import requests
import json
import telebot
from Config import  TOKEN
from Config import keys
from Config import api_key
bot=telebot.TeleBot(TOKEN)
class ConvertionException(Exception):
    pass
url=(https://api.exchangeratesapi.io/v1/convert)


class CurrencyChanger:
    @staticmethod
    def convert(quote:  str , base: str, amount:  str):
        if quote == base:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты{base}.')

        if len('values')!=3:
            raise ConvertionException('Неверное количество параметров')

        if amount('values')<1:
            raise ConvertionException('Введите корректную сумму')




        try:
            quote_ticker=keys[quote]


        except KeyError:

            raise ConvertionException(f'не удалось обработать валюту{quote}.')
        try:
            base_ticker=keys[base]

        except KeyError:

            raise ConvertionException(f'не удалось обработать валюту{base}.')

        try:
            amount = float(amount)

        except KeyError:

            raise ConvertionException(f'не удалось обработать количество {amount}.')

        quote_ticker, base_ticker = keys[quote], keys[base]


        r = request.get(f'(url) , (api_key), quote=(keys[quote_ticker] & base = (keys[base_ticker]')

        total_base = json.loads(r.content)[keys[base]]

        return total_base

