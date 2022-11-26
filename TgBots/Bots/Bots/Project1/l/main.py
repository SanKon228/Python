from cgitb import text
from email import message
import json
from re import T
from typing import Text
from aiogram import *
from aiogram import types
from aiogram.utils.markdown import hlink
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
import urllib
import os
import config
from colorama import *
from States import *
from defs import *

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

bot = Bot(token='5302355669:AAFwboWIlaCWqG-Xhg12Q2ntCCsMk3OCvH8', parse_mode='html')
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start'], state='*')
async def start(message: types.Message, state: FSMContext):
    with open('database.json', 'r') as d:
            db = json.load(d)
    if message.from_user.id not in db['users']:
        Defs().write_user(message.from_user.id) 
        Defs().write_numb(message.from_user.id) 
        await message.answer(f"Напишите номер")  
        await States.password.set()
    else:
        keyb = Defs().start_keyb()
        await message.answer(f"Marzha and procent",reply_markup=keyb)
        await States.menu1.set()

@dp.message_handler(state=States.password, content_types=types.ContentTypes.TEXT)
async def menu1(message: types.Message, state: FSMContext):
    await state.finish()
    with open('database.json', 'r') as d:
            db = json.load(d)
    if message.text == db['user-info'][str(message.from_user.id)]["number"]:
        keyb = Defs().soglasen() 
        await message.answer(f"Soglashenie",reply_markup=keyb)  
        await States.menu.set()
    else:
        await message.answer(f"Неправильный номер") 
        await message.answer(f"Напишите номер")  
        await States.password.set()


@dp.callback_query_handler(state=States.menu)
async def dani(call: types.CallbackQuery, state: FSMContext):
    callback = call.data
    await state.finish()
    if callback == 'soglasen':
        """"
        kb = KeyboardButton(text="Заказ")
        kb1 = KeyboardButton(text="История")
        kb1 = KeyboardButton(text="История")
        keyb = ReplyKeyboardMarkup(resize_keyboard=True)
        keyb.add(kb,kb1)
        keyb.add(kb2)
        """
        keyb = Defs().start_keyb()
        await call.message.answer(f"Marzha and procent",reply_markup=keyb)
        await States.menu1.set()


@dp.message_handler(state=States.menu1, content_types=types.ContentTypes.TEXT)
async def menu1(message: types.Message, state: FSMContext):
    await state.finish()
    if message.text == 'Заказ':
        keyb = Defs().nazad()
        await message.answer(f"Введите сумму",reply_markup=keyb)
        await States.zakaz.set()
    elif message.text =='История':
        with open('database.json', 'r') as d:
            db = json.load(d)
        for i in db['user-info'][str(message.from_user.id)]['zakazi']:
            keyb = Defs().start_keyb() 
            j=db['user-info'][str(message.from_user.id)]['zakazi'].index(i)
            await message.answer(text = f'Заказ {j+1} - {i}')
        await States.menu1.set()
    elif message.text =='Поддержка':
        keyb = Defs().start_keyb() 

        await message.answer(text = 'Podderzhivayu',
                                    reply_markup=keyb)
        await States.menu1.set()

        
def check_user_input(input):
    try:
        # Convert it into integer
        val = int(input)
        return True
    except ValueError:
        try:
            # Convert it into float
            val = float(input)
            return True
        except ValueError:
            return False


@dp.message_handler(state=States.zakaz, content_types=types.ContentTypes.TEXT)
async def name_step(message: types.Message, state: FSMContext):
    await state.finish()
    if message.text =='Назад':
        keyb = Defs().start_keyb() 
        await message.answer(f"Marzha and procent",reply_markup=keyb)
        await States.menu1.set()
    else:
        if check_user_input(message.text)==True:
            Defs().write_ammount(message.from_user.id,message.text)
            keyb = Defs().total() 
            await message.answer(f"это Тотал - обучение что такое ",reply_markup=keyb)
            await States.zakaz1.set()
        else:
            keyb = Defs().nazad()
            await message.answer(f"Введите сумму",reply_markup=keyb)
            await States.zakaz.set()


@dp.message_handler(state=States.zakaz1, content_types=types.ContentTypes.TEXT)
async def name_step(message: types.Message, state: FSMContext):
    await state.finish()
    if message.text == 'Да':
        keyb = Defs().start_keyb()
        await message.answer(f"Marzha and procent",reply_markup=keyb)
        await States.menu1.set()
    elif message.text =='Нет':
        #keyb = Defs().start_keyb() 
        #await call.message.answer(f"Marzha and procent",reply_markup=keyb)
        await States.menu1.set()
    elif message.text =='Назад':
        keyb = Defs().start_keyb() 
        await message.answer(f"Marzha and procent",reply_markup=keyb)
        await States.menu1.set()
""""
@dp.message_handler( message.text=='Назад', state="*")
async def nazad(message: types.Message, state: FSMContext):
    await state.finish()
    keyb = Defs().start_keyb()
    await message.answer(f"Marzha and procent",reply_markup=keyb)
    await States.menu1.set()

"""""
executor.start_polling(dp, skip_updates=True, fast=True)