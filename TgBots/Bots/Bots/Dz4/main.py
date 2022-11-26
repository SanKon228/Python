from cgitb import text
from email import message
import json
from datetime import datetime, timedelta
from re import T
from aiogram import Bot, Dispatcher, executor
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
from telegram import InputMediaPhoto
import math
import telebot
from aiogram.utils.exceptions import MessageNotModified
from contextlib import suppress

bot = Bot(token='5302355669:AAFwboWIlaCWqG-Xhg12Q2ntCCsMk3OCvH8', parse_mode='html')
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start'], state='*')
async def start(message: types.Message, state: FSMContext):
    m=['E:\HHJK\python\Bots\Dz4\zag1.jpg','E:\HHJK\python\Bots\Dz4\zag2.jpg','E:\HHJK\python\Bots\Dz4\zag3.jpg']

    k=0
    keyb=Defs().start_keyb()
    ph=m[k]
    await bot.send_photo(chat_id=message.chat.id ,photo = open(ph, 'rb'),reply_markup=keyb)  
    await States.photo.set()

@dp.callback_query_handler(state=States.photo)
async def dani2(call: types.CallbackQuery, state: FSMContext):
    m=['E:\HHJK\python\Bots\Dz4\zag1.jpg','E:\HHJK\python\Bots\Dz4\zag2.jpg','E:\HHJK\python\Bots\Dz4\zag3.jpg']
    callback = call.data
    await state.finish()
    move=callback.split('_')[0]
    k=int(callback.split('_')[1])
    if move=="left":
        if k==0:
            k = len(m)-1
            ph=m[k]
        else:
            k-=1
            ph=m[k]
        keyb=Defs().start_keyb(k)
        with suppress(MessageNotModified):
            await bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,media=InputMedia(media=open(ph, 'rb'), caption = "noitpac"),reply_markup=keyb )
        await States.photo.set()
    elif move=="right":
        m=['E:\HHJK\python\Bots\Dz4\zag1.jpg','E:\HHJK\python\Bots\Dz4\zag2.jpg','E:\HHJK\python\Bots\Dz4\zag3.jpg']
        if k==len(m)-1:
            k = 0
            ph=m[k]
        else:
            k+=1
            ph=m[k]

        keyb=Defs().start_keyb(k)
        with suppress(MessageNotModified):
            await bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,media=InputMedia(type='photo',media=open(ph, 'rb'), caption = "noitpac"),reply_markup=keyb )
        await States.photo.set()


executor.start_polling(dp, skip_updates=True, fast=True)