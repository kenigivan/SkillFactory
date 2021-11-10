# из-за новых ограничений http://api.exchangeratesapi.io бесплатного акаунта,
# а именно невозможности поменять базовую валюту (можно только конвертировать из Евро).
# пришлось применить костыль :)
import json
import requests
from config import exchanges, access_key


class APIException(Exception):
    pass


class Converter:
    @staticmethod
    def get_price(base, sym, amount):
        # print(base, sym, amount)
        try:
            base_key = exchanges[base.lower()]
        except KeyError:
            raise APIException(f"Валюта {base} не найдена!")

        try:
            sym_key = exchanges[sym.lower()]
        except KeyError:
            raise APIException(f"Валюта {sym} не найдена!")

        if base_key == sym_key:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}!')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}!')
        # Получаем стоимость одного ЕВРО за входную валюту (из которой конвертируем)
        r = requests.get(f"http://api.exchangeratesapi.io/v1/latest?access_key={access_key}&symbols={base_key}")
        resp = json.loads(r.content)
        # вычисляем сколько стоит одна входная валюта в ЕВРО:
        target_currency = 1 / resp['rates'][base_key]
        # Получаем стоимость одного ЕВРО за целевую валюту
        r = requests.get(f"http://api.exchangeratesapi.io/v1/latest?access_key={access_key}&symbols={sym_key}")
        resp = json.loads(r.content)
        # вычисляем переданное кол-во в ЕВРО (amount * target_currency) и переводим из ЕВРО в целевую валюту:
        new_price = amount * target_currency * resp['rates'][sym_key]
        new_price = round(new_price, 3)
        return new_price
