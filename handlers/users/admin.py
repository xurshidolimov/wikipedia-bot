import asyncio
import sqlite3
from aiogram.dispatcher import FSMContext
from aiogram import types
from data.config import ADMINS
from keyboards.default import admin
from loader import dp, db, bot
from states.states import SendMessage, SendReklama, SendKichikReklama
from keyboards.default import til


@dp.message_handler(commands=['admin'], user_id=ADMINS)
async def send_welcome(message: types.Message):
    await message.reply(f"Salom Wikipediauz telegram boti admin paneliga xush kelibsiz!", reply_markup=admin)


@dp.message_handler(text="🔋 Ma'lumotlar ombori", user_id=ADMINS)
async def get_all_users(message: types.Message):
    users = db.select_all_users()
    print(users[0][0])
    await message.answer(users)


@dp.message_handler(text="📊 Foydalanuvchilar soni", user_id=ADMINS)
async def count(message: types.Message):
    await message.answer(db.count_users())


@dp.message_handler(text="👤 Foydalanuvchiga xabar yuborish", user_id=ADMINS, state=None)
async def send_message_user_1(message: types.Message):
    await message.answer("Foydalanuvchi 'id'sini kiriting")
    await SendMessage.id.set()


@dp.message_handler(state=SendMessage.id)
async def send_message_user_2(message: types.Message, state: FSMContext):
    id = message.text
    await state.update_data({'id': id})
    await message.answer("Xabarni kiriting")
    await SendMessage.next()


@dp.message_handler(state=SendMessage.xabar)
async def send_message_user_3(message: types.Message, state: FSMContext):
    xabar = message.text
    await state.update_data({'xabar': xabar})

    # foydalanuvchiga yuborish
    data = await state.get_data()
    id = data['id']
    mess = data['xabar']
    await bot.send_message(chat_id=id, text=mess)

    # adminga hisobot berish
    await message.answer("Xabar yuborildi")
    await state.finish()


@dp.message_handler(text="📤 Xabar yuborish", user_id=ADMINS)
async def send_reklama(message:types.Message):
    await message.answer("Reklama yuborish uchun /pwerklsdmamdmca5sds58d3s comandasini kiriting")


@dp.message_handler(commands=['pwerklsdmamdmca5sds58d3s'], user_id=ADMINS, state=None)
async def send_message_all_user_1(message: types.Message):
    await message.answer("Xabar matnini kiriting")
    await SendReklama.rek.set()


@dp.message_handler(state=SendReklama.rek)
async def send_message_all_users_2(message: types.Message, state: FSMContext):
    rek = message.text
    await state.update_data({'rek': rek})

    # foydalanuvchilarga xabar yuborish
    data = await state.get_data()
    xat = data['rek']
    users = db.select_all_users()
    for user in users:
        user_id = user[0]
        await bot.send_message(chat_id=user_id, text=xat)
        await asyncio.sleep(0.05)

    # adminga hisobot berish
    await message.answer("Xabar yuborildi")
    await state.finish()


@dp.message_handler(text="💰 Kichik reklama", user_id=ADMINS, state=None)
async def kichikreklama1(message: types.Message):
    await message.answer('Xabar matnini kiriting')
    await SendKichikReklama.kichikreklama.set()


@dp.message_handler(state=SendKichikReklama.kichikreklama)
async def kichikreklama2(message: types.Message, state: FSMContext):
    kichikreklama = message.text

    try:
        db.delete_reklama(id=1)
        db.add_reklama(id=1, name=kichikreklama)
    except sqlite3.IntegrityError as err:
        pass

    # adminga hisobot berish
    await message.answer("Xabar saqlandi")
    await state.finish()


@dp.message_handler(text="💰 Kichik reklamani o'chirish", user_id=ADMINS)
async def delete_reklama(message:types.Message):
    db.delete_reklama(id=1)
    await message.answer("Kichik reklama o'chirildi")


@dp.message_handler(text="◀️Ortga", user_id=ADMINS)
async def delete_reklama(message:types.Message):
    user = db.select_user(id=message.from_user.id)
    language = user[2]

    if language == 'uz':
        await message.answer("Maqola mavzusini yuboring", reply_markup=til)
    elif language == 'ru':
        await message.answer("Отправить текст статьи", reply_markup=til)
    else:
        await message.answer("Send article subject", reply_markup=til)
