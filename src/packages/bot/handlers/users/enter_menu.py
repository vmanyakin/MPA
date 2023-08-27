from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from src.packages.bot.keyboards import hello_keyboard
from src.packages.bot.loader import dispatcher, load_json, template_json


@dispatcher.message_handler(CommandStart)
async def hello(message: types.Message):
    user_id = str(message.from_user.id)
    text = template_json(load_json["enter_menu"]["hello"]).render(user_id=user_id)
    print(text)
    await message.answer(user_id, reply_markup=hello_keyboard)
