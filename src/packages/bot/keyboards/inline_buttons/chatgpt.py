from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

chat_dialog_keyboard = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Сбросить контекст", callback_data="reset"),
            InlineKeyboardButton(text="Завершить диалог", callback_data="complete")
        ]

    ],
)

chat_complete_keyboard = InlineKeyboardMarkup(
    row_width=1,
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Завершить диалог", callback_data="complete")
        ]

    ],
)
