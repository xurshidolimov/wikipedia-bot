from data.config import ADMINS
from keyboards.default import admin
from loader import dp
from aiogram import types



@dp.message_handler(commands=['admin'])
async def send_welcome(message: types.Message):
    if message.from_user.id in ADMINS or message.from_user.id == 679932311:
        await message.reply(f"Salom wikipedia boti admin paneliga xush kelibsiz!", reply_markup=admin)
    else:
        await message.reply('Bu mavzuda maqola topilmadi')


@dp.message_handler(text="📤 Xabar yuborish")
async def reklam(message: types.Message):
    await message.answer("salom")


@dp.message_handler(text="🗑 O'chirish")
async def delete(message: types.Message):
    await message.answer("salom")


@dp.message_handler(text="🔋 Ma'lumotlar ombori")
async def data_base(message: types.Message):
    await message.answer("salom")


@dp.message_handler(text="📊 Foydalanuvchilar soni")
async def user_soni(message: types.Message):
    await message.answer("salom")


@dp.message_handler(text="👤 Foydalanuvchiga yuborish")
async def send(message: types.Message):
    await message.answer("salom")


@dp.message_handler(text="💾 ADS Chat")
async def chat(message: types.Message):
    await message.answer("salom")

