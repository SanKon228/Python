import json
import requests
from aiogram.types import *
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
import random

def rand():
    str1 = '123456789'
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    str3 = str2.upper()
    print(str3)
    str4 = str1+str2+str3
    print(str4)
    ls = list(str4)
    random.shuffle(ls)
    psw = ''.join([random.choice(ls) for x in range(10)])
    #return psw
    with open('database.json', 'r') as d:
        db = json.load(d)
    k=False
    for i in db["numbers"]:
        if psw==i:
            k=True
    if k==True:
        rand()
    else:
        
        return psw




class Defs:
    @staticmethod
    def soglasen():
        soglasen = InlineKeyboardButton(text='Согласен', callback_data='soglasen')
        keyb = InlineKeyboardMarkup()
        keyb.add(soglasen)
        return keyb
    @staticmethod
    def start_keyb():
        kb = KeyboardButton(text="Заказ")
        kb1 = KeyboardButton(text="История")
        
        kb2= KeyboardButton(text="Поддержка")
        
        
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(kb,kb1)
        keyboard.add(kb2)
        return keyboard
    @staticmethod
    def total():
        da = KeyboardButton(text='Да')
        net = KeyboardButton(text='Нет')
        nazad = KeyboardButton(text='Назад')
        keyb = ReplyKeyboardMarkup(resize_keyboard=True)
        keyb.add(da,net)
        keyb.add(nazad)
        return keyb
    
    @staticmethod
    def nazad():
        nazad = KeyboardButton(text='Назад')
        keyb = ReplyKeyboardMarkup(resize_keyboard=True)
        keyb.add(nazad)
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
        db['user-info'][str(id)] = {"zakazi": [],
                                    "number": ""}
        with open('database.json', 'w') as d:
            json.dump(db, d, indent=3)
    @staticmethod
    def write_numb(id):
        with open('database.json', 'r') as d:
            db = json.load(d)
        numb = rand()
        db['user-info'][str(id)]["number"]=f"{numb}"
        db["numbers"].append(numb)
        with open('database.json', 'w') as d:
            json.dump(db, d, indent=3)
    
    @staticmethod
    def write_ammount(id,ammount):
        with open('database.json', 'r') as d:
            db = json.load(d)
        db['user-info'][str(id)]["zakazi"].append(ammount)
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

    