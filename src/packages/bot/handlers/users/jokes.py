"""
Setting up commands for jokes
"""

from random import randint

from aiogram import types

from src.packages.bot.keyboards import jokes_start_keyboard, jokes_data_keyboard
from src.packages.bot.loader import bot, dispatcher, load_text_messages, template_json, load_jokes
from src.packages.database.mongodb import UsersCollection


@dispatcher.callback_query_handler(text="Анекдоты")
async def jokes_start(call: types.CallbackQuery):
    await UsersCollection.add(call.from_user.id, call.message.chat.id, call.from_user.first_name,
                              call.from_user.last_name, call.from_user.username, call.data)
    text_jokes_start = template_json(
        load_text_messages["jokes"]["jokes_start"] + load_text_messages["jokes"]["label"]).render()
    await call.message.answer(text_jokes_start, reply_markup=jokes_start_keyboard)


@dispatcher.callback_query_handler(text="joke")
async def jokes_data(call: types.CallbackQuery):
    key_in_data_json = str(randint(1, 150))
    joke = load_jokes[key_in_data_json]
    text_cinema_data = template_json(
        load_text_messages["jokes"]["jokes_data"] + load_text_messages["jokes"]["label"]).render(joke=joke)
    await bot.edit_message_text(text_cinema_data, chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                reply_markup=jokes_data_keyboard)
