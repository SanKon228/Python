import json
import requests
from aiogram.types import *


class Defs:
    @staticmethod
    def start_keyb(index=0):
        m=['E:\HHJK\python\Bots\Dz4\zag1.jpg','E:\HHJK\python\Bots\Dz4\zag2.jpg','E:\HHJK\python\Bots\Dz4\zag3.jpg']
        if index < 0:
            index = len(m) - 1
        if index > len(m)-1:
            index = 0
        left = InlineKeyboardButton(text='⬅️', callback_data=f'left_{index}')
        right = InlineKeyboardButton(text='➡️', callback_data=f'right_{index}')
        keyb = InlineKeyboardMarkup()
        keyb.row(left, right)
        return keyb

    @staticmethod
    def get_ph(index=0):
        m=['E:\HHJK\python\Bots\Dz4\zag1.jpg','E:\HHJK\python\Bots\Dz4\zag2.jpg','E:\HHJK\python\Bots\Dz4\zag3.jpg']
        if index < 0:
            index = len(m) - 1
        if index == len(m):
            index = 0
        print(f"index {index}")
        return m[index]
