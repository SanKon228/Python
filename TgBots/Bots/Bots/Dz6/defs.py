import json
import requests
from aiogram.types import *


class Defs:
    @staticmethod
    def start_keyb():
        
        pokazat = InlineKeyboardButton(text='Pokazat', callback_data='pokazat')
        perepisat = InlineKeyboardButton(text='Zanovo', callback_data='perepisat')
        keyb = InlineKeyboardMarkup()
        keyb.row(pokazat, perepisat)
        return keyb
    @staticmethod
    def choose_keyb():
        da = InlineKeyboardButton(text='da', callback_data='da')
        net = InlineKeyboardButton(text='net', callback_data='net')
        keyb = InlineKeyboardMarkup()
        keyb.row(da,net)
        return keyb
    @staticmethod
    def pok1_keyb():
        pokazat = InlineKeyboardButton(text='Pokazat', callback_data='pokazat2')
        soob = InlineKeyboardButton(text='soob', callback_data='soob')
        keyb = InlineKeyboardMarkup()
        keyb.row(pokazat,soob)
        return keyb
    @staticmethod
    def pok_keyb():
        pokazat = InlineKeyboardButton(text='Pokazat', callback_data='pokazat2')
        keyb = InlineKeyboardMarkup()
        keyb.row(pokazat)
        return keyb    
    @staticmethod
    def zan_keyb():
        perepisat = InlineKeyboardButton(text='Zanovo', callback_data='perepisat')
        keyb = InlineKeyboardMarkup()
        keyb.row( perepisat)
        return keyb
    
    @staticmethod
    def write_user(id):
        with open('database.json', 'r') as d:
            db = json.load(d)
        if id not in db['users']:
            db['users'].append(id)
        db['user-info'][str(id)] = {"name":"","fname":"","age":""}
        with open('database.json', 'w') as d:
            json.dump(db, d, indent=3)
    
    @staticmethod
    def write_name(id,name):
        with open('database.json', 'r') as d:
            db = json.load(d)
        db['user-info'][str(id)]['name']=name
        with open('database.json', 'w') as d:
            json.dump(db, d, indent=3)
    
    @staticmethod
    def write_fname(id,fname):
        with open('database.json', 'r') as d:
            db = json.load(d)
        db['user-info'][str(id)]['fname']=fname
        with open('database.json', 'w') as d:
            json.dump(db, d, indent=3)
    
    @staticmethod
    def write_age(id,age):
        with open('database.json', 'r') as d:
            db = json.load(d)
        db['user-info'][str(id)]['age']=age
        with open('database.json', 'w') as d:
            json.dump(db, d, indent=3)

    