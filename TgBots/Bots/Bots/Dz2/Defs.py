import json
import requests
from aiogram.types import *

class Defs:
    @staticmethod
    def starter_keyb():
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        button_1 = KeyboardButton(text="da")
        keyboard.add(button_1)
        button_2 = "ne"
        keyboard.add(button_2)
        return keyboard
    
    @staticmethod
    def eshcho_keyb():
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        button_1 = KeyboardButton(text="eshcho")
        keyboard.add(button_1)
        return keyboard
    
    @staticmethod
    def esli_keyb():
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        button_1 = KeyboardButton(text="Nu esli chto tikay")
        keyboard.add(button_1)
        return keyboard