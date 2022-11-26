import json
import requests
from aiogram.types import *


class Defs:
    @staticmethod
    def start_keyb(k):
        
        left = InlineKeyboardButton(text='⬅️', callback_data=f'left_{k}')
        right = InlineKeyboardButton(text='➡️', callback_data=f'right_{k}')
        keyb = InlineKeyboardMarkup()
        keyb.row(left, right)
        return keyb

    @staticmethod
    def lol(k):
        m=['E:\HHJK\python\Bots\Dz4\zag1.jpg','E:\HHJK\python\Bots\Dz4\zag2.jpg','E:\HHJK\python\Bots\Dz4\zag3.jpg']
        return m[k]