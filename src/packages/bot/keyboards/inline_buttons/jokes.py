from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

jokes_start_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Поехали!", callback_data="joke")
        ]

    ],
)
jokes_data_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Ещё анекдот!", callback_data="joke")
        ],
        [
            InlineKeyboardButton(text="Меню", callback_data="menu")
        ]

    ],
)
