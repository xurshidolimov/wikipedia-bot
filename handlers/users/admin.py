import asyncio

from aiogram.dispatcher import FSMContext
from aiogram import types
from data.config import ADMINS
from keyboards.default import admin
from loader import dp, db, bot
from states.states import SendMessage, SendReklama, SendKichikReklama

@dp.message_handler(commands=['admin'], user_id=ADMINS)
async def send_welcome(message: types.Message):
    if message.from_user.id in ADMINS or message.from_user.id == 679932311:
        await message.reply(f"Salom Wikipediauz telegram boti admin paneliga xush kelibsiz!", reply_markup=admin)
    else:
        await message.reply('Bu mavzuda maqola topilmadi')


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
    await state.update_data({'kichikreklama': kichikreklama})
    data = await state.get_data()
    xat = data['kichikreklama']
    box = xat

    # adminga hisobot berish
    await message.answer("Xabar saqlandi")
    await state.finish()
    return box