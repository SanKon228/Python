import json
import codecs
import asyncio
from datetime import datetime, timedelta
from aiogram import Bot, Dispatcher, executor
from aiogram import types
from aiogram.utils.markdown import hlink
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
import urllib
import os
from aiogram.dispatcher.filters import Text
from colorama import *
from urllib import response
import requests
import asyncio
from Defs import *
from State import *
import time
from bs4 import BeautifulSoup


bot = Bot(token='5302355669:AAFwboWIlaCWqG-Xhg12Q2ntCCsMk3OCvH8', parse_mode='html')
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start'], state='*')
async def start(message: types.Message, state: FSMContext):
    
    keyboard = Defs().starter_keyb()
    await message.answer(f"Sumno?",reply_markup=keyboard)
    await state.finish()
    await States.start_kit.set()

photo="sample_image.png"

@dp.message_handler(state=States.start_kit)
async def yes_or_no(message: types.Message, state: FSMContext):
    msg = message.text
    await state.finish()
    if msg == 'da' :
        url='https://thiscatdoesnotexist.com/'
        response = requests.get(url)

        with open("E:\HHJK\python\Bots\Dz2\sample_image.png", "wb") as file:
            file.write(response.content)
        await bot.send_photo(chat_id=message.chat.id ,photo = open("E:\HHJK\python\Bots\Dz2\sample_image.png", 'rb'))
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ["eshcho", "ne"]
        keyboard.add(*buttons)
        await message.answer("Успокоить?", reply_markup=keyboard)
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        await States.start_kit.set()
    elif msg == 'eshcho':
        url='https://thiscatdoesnotexist.com/'
        response = requests.get(url)

        with open("E:\HHJK\python\Bots\Dz2\sample_image.png", "wb") as file:
            file.write(response.content)
        keyboard = types.InlineKeyboardMarkup()

        await bot.send_photo(chat_id=message.chat.id ,photo = open("E:\HHJK\python\Bots\Dz2\sample_image.png", 'rb'))
        await States.start_kit.set()
    elif msg == 'ne':
        await message.reply("Если буду нужен нажми /start , пока✋", reply_markup=types.ReplyKeyboardRemove())
    

executor.start_polling(dp, skip_updates=True, fast=True)