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
        KeyboardButton(text="🔋 Ma'lumotlar ombori"),
        ],
        [
        KeyboardButton(text="👤 Foydalanuvchiga xabar yuborish"),
        KeyboardButton(text="📊 Foydalanuvchilar soni"),
        ],
        [
        KeyboardButton(text="💰 Kichik reklama"),
        KeyboardButton(text="💰 Kichik reklamani o'chirish"),
        ],
        [
        KeyboardButton(text="◀️Ortga"),
        ]
    ], resize_keyboard=True
)
