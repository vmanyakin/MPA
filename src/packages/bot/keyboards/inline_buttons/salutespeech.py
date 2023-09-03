from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

salutespeech_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Меню", callback_data="menu")
        ]

    ],
)
