from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

til = ReplyKeyboardMarkup(
    keyboard=[
        [
        KeyboardButton(text="🇺🇿 o'zbekcha"),
        KeyboardButton(text="🇬🇧 english"),
        KeyboardButton(text="🇷🇺 русский")
        ]
    ], resize_keyboard=True
)

admin = ReplyKeyboardMarkup(
    keyboard=[
        [
        KeyboardButton(text="📤 Xabar yuborish"),
        KeyboardButton(text="🗑 O'chirish"),
        ],
        [
        KeyboardButton(text="🔋 Ma'lumotlar ombori"),
        KeyboardButton(text="📊 Foydalanuvchilar soni"),
        ],
        [
        KeyboardButton(text="👤 Foydalanuvchiga yuborish"),
        KeyboardButton(text="💾 ADS Chat"),
        ]
    ], resize_keyboard=True
)