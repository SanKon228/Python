import json
from datetime import datetime, timedelta
from platform import python_branch
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

BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
if not BOT_TOKEN:
    raise RuntimeError('Set TELEGRAM_BOT_TOKEN environment variable')
bot = Bot(token=BOT_TOKEN, parse_mode='html')
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'], state='*')
async def start(message: types.Message, state: FSMContext):
    await state.finish()
    Defs().write_user(message.from_user.id)
    keyb = Defs().start_keyb()
    await message.answer('РџСЂРёРІС–С‚ РѕР±РµСЂРё С‰Рѕ Р±Р°Р¶Р°С”С€', reply_markup=keyb)
    await States.food_state.set()


@dp.callback_query_handler(state=States.food_state)
async def what_u_want(call: types.CallbackQuery, state: FSMContext):
    callback = call.data
    await state.finish()
    if callback == 'sushi':
        keyb = Defs().size_keyb()
        Defs().write_food(call.from_user.id, callback)
        await bot.edit_message_text(chat_id=call.from_user.id
                                    , message_id=call.message.message_id,
                                    text='Р’Р°С€ РІРёР±С–СЂ Р·Р°РїРёСЃР°РЅРѕ , РѕР±РµСЂС–С‚СЊ Р±СѓРґСЊР»Р°СЃРєР° СЂРѕР·РјС–СЂ',
                                    reply_markup=keyb)
        await States.size_state.set()
    elif callback == 'pizza':
        keyb = Defs().size_keyb()
        Defs().write_food(call.from_user.id, callback)
        await bot.edit_message_text(chat_id=call.from_user.id
                                    , message_id=call.message.message_id,
                                    text='Р’Р°С€ РІРёР±С–СЂ Р·Р°РїРёСЃР°РЅРѕ , РѕР±РµСЂС–С‚СЊ Р±СѓРґСЊР»Р°СЃРєР° СЂРѕР·РјС–СЂ',
                                    reply_markup=keyb)
        await States.size_state.set()

    elif callback == 'icecream':
        keyb = Defs().size_keyb()
        Defs().write_food(call.from_user.id, callback)
        await bot.edit_message_text(chat_id=call.from_user.id
                                    , message_id=call.message.message_id,
                                    text='Р’Р°С€ РІРёР±С–СЂ Р·Р°РїРёСЃР°РЅРѕ , РѕР±РµСЂС–С‚СЊ Р±СѓРґСЊР»Р°СЃРєР° СЂРѕР·РјС–СЂ',
                                    reply_markup=keyb)
        await States.size_state.set()


@dp.callback_query_handler(state=States.size_state)
async def size_get(call: types.CallbackQuery, state: FSMContext):
    callback = call.data
    await state.finish()
    if callback == 'small':
        keyb = Defs().geolocation()
        Defs().write_size(call.from_user.id, callback)
        await call.message.answer(text='Р”СЏРєСѓСЋ РІРё Р·Р°РїРѕРІРЅРёР»Рё РІСЃС– РґР°РЅРЅС–',reply_markup=keyb)
        await States.geo.set()
    elif callback == 'medium':
        keyb = Defs().geolocation()
        Defs().write_size(call.from_user.id, callback)
        await call.message.answer(text='Р”СЏРєСѓСЋ РІРё Р·Р°РїРѕРІРЅРёР»Рё РІСЃС– РґР°РЅРЅС–',reply_markup=keyb)

        await States.geo.set()

    elif callback == 'large':
        keyb = Defs().geolocation()
        Defs().write_size(call.from_user.id, callback)
        await call.message.answer(text='Р”СЏРєСѓСЋ РІРё Р·Р°РїРѕРІРЅРёР»Рё РІСЃС– РґР°РЅРЅС–',reply_markup=keyb)

        await States.geo.set()

    elif callback == 'back':
        keyb = Defs().start_keyb()
        await bot.edit_message_text(chat_id=call.from_user.id,message_id=call.message.message_id
                                    ,text = 'РџСЂРёРІС–С‚ РѕР±РµСЂРё С‰Рѕ Р±Р°Р¶Р°С”С€',reply_markup=keyb)
        await States.food_state.set()


@dp.message_handler(content_types=['location'], state=States.geo)
async def handle_location(message: types.Message):
    lat = message.location.latitude
    lon = message.location.longitude
    reply = "latitude:  {}\nlongitude: {}".format(lat, lon)
    await message.answer(reply)
 

executor.start_polling(dp, skip_updates=True, fast=True)

