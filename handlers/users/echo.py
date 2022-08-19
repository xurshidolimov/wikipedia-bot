import sqlite3

from aiogram import types
import wikipedia
from utils.db_api.sqlite import box
from data.config import ADMINS
from loader import dp, db, bot


@dp.message_handler(text="🇺🇿 o'zbekcha")
async def language(message: types.Message):
    name = message.from_user.full_name
    wikipedia.set_lang('uz')
    await message.answer(f"Salom {message.from_user.full_name}! \nMaqola mavzusini yuboring")
    try:
        db.add_user(id=message.from_user.id,
                    name=name)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS[0], text=err)


@dp.message_handler(text="🇬🇧 english")
async def language(message: types.Message):
    name = message.from_user.full_name
    wikipedia.set_lang('en')
    await message.answer(f"Hi {message.from_user.full_name}! \nSend article subject")
    try:
        db.add_user(id=message.from_user.id,
                    name=name)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS[0], text=err)


@dp.message_handler(text="🇷🇺 русский")
async def language(message: types.Message):
    name = message.from_user.full_name
    wikipedia.set_lang('ru')
    await message.answer(f"Привет {message.from_user.full_name}! \nОтправить текст статьи")
    try:
        db.add_user(id=message.from_user.id,
                    name=name)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS[0], text=err)


@dp.message_handler()
async def sendwiki(message: types.Message):
    name = message.from_user.full_name
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
        await message.answer(box)
    except:
        await message.answer("Bu mavzuga oid maqola topilmadi "
                             "\nNo article found for this topic"
                             "\nНе найдена статья по этой теме")
    try:
        db.add_user(id=message.from_user.id,
                    name=name)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS[0], text=err)
