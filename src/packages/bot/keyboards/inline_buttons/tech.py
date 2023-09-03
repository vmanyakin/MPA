from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

tech_start_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Мой id", callback_data="id"),
            InlineKeyboardButton(text="Id стикера", callback_data="sticker")
        ]

    ],
)

tech_menu_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Меню", callback_data="menu")
        ]

    ],
)