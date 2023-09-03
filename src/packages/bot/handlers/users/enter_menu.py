from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from random import choice
from src.packages.bot.keyboards import hello_keyboard
from src.packages.bot.loader import bot, dispatcher, load_text_messages, template_json


@dispatcher.message_handler(CommandStart())
async def hello(message: types.Message):
    first_name = str(message.from_user.first_name)
    text_hello = template_json(load_text_messages["enter_menu"]["hello"] + load_text_messages["label_MPA"]).render(first_name=first_name)
    await message.answer(text_hello, reply_markup=hello_keyboard)


@dispatcher.message_handler()
@dispatcher.callback_query_handler(text="menu")
async def menu(call: types.Message):
    chat_id = call.message.chat.id if isinstance(call, types.CallbackQuery) else call.chat.id
    random_text = choice(load_text_messages["enter_menu"]["menu"])
    text_menu = template_json(random_text + load_text_messages["label_MPA"]).render()
    await bot.send_message(chat_id=chat_id, text=text_menu, reply_markup=hello_keyboard)
