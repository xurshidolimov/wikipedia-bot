from aiogram import types
import wikipedia
from loader import dp

@dp.message_handler(text="🇺🇿 o'zbekcha")
async def language(message: types.Message):
    wikipedia.set_lang('uz')
    await message.answer(f"Salom {message.from_user.full_name}! \nMaqola mavzusini yuboring")


@dp.message_handler(text="🇬🇧 english")
async def language(message: types.Message):
    wikipedia.set_lang('en')
    await message.answer(f"Hi {message.from_user.full_name}! \nSend article subject")


@dp.message_handler(text="🇷🇺 русский")
async def language(message: types.Message):
    wikipedia.set_lang('ru')
    await message.answer(f"Привет {message.from_user.full_name}! \nОтправить текст статьи")


@dp.message_handler()
async def sendwiki(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer("Bu mavzuga oid maqola topilmadi "
                             "\nNo article found for this topic"
                             "\nНе найдена статья по этой теме")

