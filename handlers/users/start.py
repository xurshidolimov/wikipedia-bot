from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default import til
from loader import dp

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer('Tilni tanlang \nChoose language \nВыберите язык', reply_markup=til)

