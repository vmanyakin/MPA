from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from src.packages.bot.keyboards import hello_keyboard
from src.packages.bot.loader import dispatcher, load_json, template_json


@dispatcher.message_handler(CommandStart())
async def hello(message: types.Message):
    user_id = str(message.from_user.id)
    text_hello = template_json(load_json["enter_menu"]["hello"] + load_json["label_MPA"]).render(user_id=user_id)
    await message.answer(text_hello, reply_markup=hello_keyboard)
