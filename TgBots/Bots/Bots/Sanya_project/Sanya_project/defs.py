import json
import requests
from aiogram.types import *


class Defs:
    @staticmethod
    def start_keyb():
        sushi = InlineKeyboardButton(text='Суши', callback_data='sushi')
        pizza = InlineKeyboardButton(text='Піца', callback_data='pizza')
        iceCream = InlineKeyboardButton(text='Морозиво', callback_data='icecream')
        keyb = InlineKeyboardMarkup()
        keyb.row(sushi, pizza)
        keyb.add(iceCream)
        return keyb

    @staticmethod
    def write_user(id):
        with open('database.json', 'r') as d:
            db = json.load(d)
        if id not in db['users']:
            db['users'].append(id)
        db['user-info'][str(id)] = {"food": "",
                                    "size": ""}
        with open('database.json', 'w') as d:
            json.dump(db, d, indent=3)

    @staticmethod
    def write_food(id, food):
        with open('database.json', 'r') as d:
            db = json.load(d)
        db['user-info'][str(id)]['food'] = food
        with open('database.json', 'w') as d:
            json.dump(db, d, indent=3)

    @staticmethod
    def size_keyb():
        small = InlineKeyboardButton(text='Маленький', callback_data='small')
        medium = InlineKeyboardButton(text='Cередній', callback_data='medium')
        large = InlineKeyboardButton(text='Великий', callback_data='large')
        back = InlineKeyboardButton(text='Назад', callback_data='back')
        keyb = InlineKeyboardMarkup()
        keyb.add(small)
        keyb.add(medium)
        keyb.add(large)
        keyb.add(back)
        return keyb

    @staticmethod
    def write_size(id, size):
        with open('database.json', 'r') as d:
            db = json.load(d)
        db['user-info'][str(id)]['size'] = size
        with open('database.json', 'w') as d:
            json.dump(db, d, indent=3)
    @staticmethod
    def geolocation():
        geo = KeyboardButton('Надіслати своє місцеположення',request_location=True)
        keyb = ReplyKeyboardMarkup(resize_keyboard=True)
        keyb.add(geo)
        return keyb