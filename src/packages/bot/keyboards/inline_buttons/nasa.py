from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

nasa_start_keyboard = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Начнём!", callback_data="start")
        ]

    ],
)

nasa_data_keyboard = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Хочу ещё!", callback_data="forth"),
            InlineKeyboardButton(text="Завершить", callback_data="complete")
        ]

    ],
)
