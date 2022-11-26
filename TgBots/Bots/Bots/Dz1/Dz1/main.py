import json
from datetime import datetime, timedelta
from aiogram import Bot, Dispatcher, executor
from aiogram import types
from aiogram.utils.markdown import hlink
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
import urllib
import os
from colorama import *
from States import *
from defs import *

bot = Bot(token='5302355669:AAFwboWIlaCWqG-Xhg12Q2ntCCsMk3OCvH8', parse_mode='html')
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start'], state='*')
async def start(message: types.Message, state: FSMContext):
      
    with open('database.json', 'r') as d:
            db = json.load(d)
    if message.from_user.id not in db['users']:
        await message.answer(f"Вас немає в базі даних \nДавайте створимо ваш акаунт")
        Defs().write_user(message.from_user.id)
        await message.answer(f"Name")
        await States.name.set()
    else:
        keyb = Defs().start_keyb()
        await message.answer('Привіт обери що hosh', reply_markup=keyb)
        await States.dani.set()
     
    
@dp.message_handler(state=States.name, content_types=types.ContentTypes.TEXT)
async def name_step(message: types.Message, state: FSMContext):
    Defs().write_name(message.from_user.id,message.text)
    await message.answer(f"Записано")
    await message.answer(f"Familia")
    await state.finish()
    await States.fname.set()

@dp.callback_query_handler(state=States.dani)
async def dani(call: types.CallbackQuery, state: FSMContext):
    callback = call.data
    await state.finish()
    if callback == 'pokazat':
        with open('database.json', 'r') as d:
            db = json.load(d)
        name = db['user-info'][str(call.from_user.id)]['name']
        fname = db['user-info'][str(call.from_user.id)]['fname']
        age = db['user-info'][str(call.from_user.id)]['age']
        keyb = Defs().start_keyb()
        await bot.edit_message_text(chat_id=call.from_user.id,
                                    message_id=call.message.message_id
                                    ,text = '{},{},{}'.format(name,fname,age),
                                    reply_markup=keyb)
        
        await States.dani2.set()

    elif callback == 'perepisat':
        await call.message.answer(f"Name")
        await States.name.set()
    elif callback == 'pokazat2':
        with open('database.json', 'r') as d:
            db = json.load(d)
        name = db['user-info'][str(call.from_user.id)]['name']
        fname = db['user-info'][str(call.from_user.id)]['fname']
        age = db['user-info'][str(call.from_user.id)]['age']
        keyb = Defs().zan_keyb()
        await bot.edit_message_text(chat_id=call.from_user.id,
                                    message_id=call.message.message_id
                                    ,text = '{},{},{}'.format(name,fname,age),
                                    reply_markup=keyb)
        
        await States.dani.set()

@dp.callback_query_handler(state=States.dani2)
async def dani2(call: types.CallbackQuery, state: FSMContext):
    callback = call.data
    await state.finish()
    if callback == 'pokazat':
        with open('database.json', 'r') as d:
            db = json.load(d)
        name = db['user-info'][str(call.from_user.id)]['name']
        fname = db['user-info'][str(call.from_user.id)]['fname']
        age = db['user-info'][str(call.from_user.id)]['age']
        keyb = Defs().zan_keyb()
        await bot.edit_message_text(chat_id=call.from_user.id,
                                    message_id=call.message.message_id
                                    ,text = '{},{},{}'.format(name,fname,age),
                                    reply_markup=keyb)
        
        await States.dani.set()

@dp.message_handler(state=States.fname, content_types=types.ContentTypes.TEXT)
async def fname_step(message: types.Message, state: FSMContext):
    await message.answer(f"Записано")
    Defs().write_fname(message.from_user.id,message.text)
    await message.answer(f"age")
    await state.finish()
    await States.age.set()


@dp.message_handler(state=States.age, content_types=types.ContentTypes.TEXT)
async def age_step(message: types.Message, state: FSMContext):
    Defs().write_age(message.from_user.id,message.text)
    keyb = Defs().pok_keyb()
    await message.answer(f"Записано",reply_markup=keyb)
    
    await States.dani.set()
    
    





executor.start_polling(dp, skip_updates=True, fast=True)