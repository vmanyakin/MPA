from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

cinema_data_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Фильм", callback_data="Фильм"),
            InlineKeyboardButton(text="Сериал", callback_data="Сериал"),
        ],
        [
            InlineKeyboardButton(text="Мультфильм", callback_data="Мультфильм"),
            InlineKeyboardButton(text="Аниме", callback_data="Аниме"),
        ],
        [
            InlineKeyboardButton(text="Меню", callback_data="menu")
        ]

    ],
)
