from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

hello_keyboard = InlineKeyboardMarkup(
    row_width=3,
    inline_keyboard=[
        [
            InlineKeyboardButton(text="ChatGPT", callback_data="ChatGPT"),
            InlineKeyboardButton(text="NASA", callback_data="NASA"),
            InlineKeyboardButton(text="Кинопоиск", callback_data="Кинопоиск"),
        ],
        [
            InlineKeyboardButton(text="SaluteSpeech", callback_data="SaluteSpeech"),
            InlineKeyboardButton(text="Анекдот", callback_data="Анекдот"),
            InlineKeyboardButton(text="Тех", callback_data="Тех"),
        ]

    ],
)
