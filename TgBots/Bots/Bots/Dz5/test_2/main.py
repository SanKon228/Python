from aiogram import Bot, Dispatcher, executor
from aiogram import types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from States import *
from defs import *
from telegram import InputMediaPhoto
from aiogram.utils.exceptions import MessageNotModified
from contextlib import suppress

bot = Bot(token='5302355669:AAFwboWIlaCWqG-Xhg12Q2ntCCsMk3OCvH8', parse_mode='html')
dp = Dispatcher(bot, storage=MemoryStorage())



@dp.message_handler(commands=['start'], state='*')
async def start(message: types.Message, state: FSMContext):
    k = 0
    m=['E:\HHJK\python\Bots\Dz4\zag1.jpg','E:\HHJK\python\Bots\Dz4\zag2.jpg','E:\HHJK\python\Bots\Dz4\zag3.jpg']
    ph = m[k]
    keyb = Defs.start_keyb()
    await bot.send_photo(chat_id=message.chat.id, photo=open(ph, 'rb'), reply_markup=keyb)
    await States.photo.set()


@dp.callback_query_handler(state=States.photo)
async def dani2(call: types.CallbackQuery, state: FSMContext):
    m=['E:\HHJK\python\Bots\Dz4\zag1.jpg','E:\HHJK\python\Bots\Dz4\zag2.jpg','E:\HHJK\python\Bots\Dz4\zag3.jpg']
    callback = call.data
    await state.finish()

    move = callback.split('_')[0]
    index = int(callback.split('_')[1])
    if move == "left":
        index -=1
        ph = Defs().get_ph(index)
        keyb = Defs.start_keyb(index)
        with suppress(MessageNotModified):
            await bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                         media=InputMedia(media=open(ph, 'rb'), caption="noitpac"), reply_markup=keyb)
        await States.photo.set()
    elif move == "right":
        index +=1
        ph = Defs().get_ph(index)
        keyb = Defs.start_keyb(index)
        with suppress(MessageNotModified):
            await bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                         media=InputMedia(type='photo', media=open(ph, 'rb'), caption="noitpac"),
                                         reply_markup=keyb)
        await States.photo.set()


executor.start_polling(dp, skip_updates=True, fast=True)
