from aiogram import types
from loader import dp, db
import wikipedia


@dp.message_handler(text="🇺🇿 o'zbekcha")
async def language_uz(message: types.Message):
    db.update_user_language(language='uz', id=message.from_user.id)
    await message.answer("Maqola mavzusini yuboring")


@dp.message_handler(text="🇬🇧 english")
async def language_en(message: types.Message):
    db.update_user_language(language='en', id=message.from_user.id)
    await message.answer("Send article subject")


@dp.message_handler(text="🇷🇺 русский")
async def language_ru(message: types.Message):
    db.update_user_language(language='ru', id=message.from_user.id)
    await message.answer("Отправить текст статьи")


@dp.message_handler()
async def sendwiki(message: types.Message):
    user = db.select_user(id=message.from_user.id)
    language = user[2]
    try:
        wikipedia.set_lang(language)
        respond = wikipedia.summary(message.text)
        await message.answer(respond)

# ------kichik reklama yuborish ---------------------------------
        reklama=db.select_reklama()
        if reklama:
            reklama=str(reklama)
            await message.answer(reklama[3: -4])
# ---------------------------------------------------------------
    except:
        if language=='uz':
            await message.answer("Bu mavzuga oid maqola topilmadi ")
        elif language=='ru':
            await message.answer("Не найдена статья по этой теме")
        else:
            await message.answer("No article found for this topic")

