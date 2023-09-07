"""
Setting up commands for cinema
"""

from random import randint

from aiogram import types

from src.packages.bot.keyboards import cinema_data_keyboard
from src.packages.bot.loader import bot, dispatcher, load_text_messages, template_json, load_films, load_serials, \
    load_cartoons, load_anime
from src.packages.database.mongodb import UsersCollection


@dispatcher.callback_query_handler(text="Кинопоиск")
async def cinema_start(call: types.CallbackQuery):
    await UsersCollection.add(call.from_user.id, call.message.chat.id, call.from_user.first_name,
                              call.from_user.last_name, call.from_user.username, call.data)
    text_cinema_start = template_json(
        load_text_messages["cinema"]["cinema_start"] + load_text_messages["cinema"]["label"]).render()
    await call.message.answer(text_cinema_start, reply_markup=cinema_data_keyboard)


@dispatcher.callback_query_handler(
    lambda callback_query: callback_query.data in ["Фильм", "Сериал", "Мультфильм", "Аниме"])
async def cinema_data(call: types.CallbackQuery):
    key_in_data_json = str(randint(1, 250))
    if call.data == "Аниме":
        data = load_anime[key_in_data_json]
    elif call.data == "Сериал":
        data = load_serials[key_in_data_json]
    elif call.data == "Мультфильм":
        data = load_cartoons[key_in_data_json]
    else:
        data = load_films[key_in_data_json]
    title = data["title"]
    genre = data["genre"]
    director = data["director"]
    country = data["country"]
    year = data["year"]
    duration = data["duration"]
    rating = data["rating"] + "⭐️"
    trailer = data["trailer"]
    text_cinema_data = template_json(
        load_text_messages["cinema"]["cinema_data"] + load_text_messages["cinema"]["label"]).render(title=title,
                                                                                                    genre=genre,
                                                                                                    director=director,
                                                                                                    country=country,
                                                                                                    year=year,
                                                                                                    duration=duration,
                                                                                                    rating=rating,
                                                                                                    trailer=trailer)
    await bot.edit_message_text(text_cinema_data, chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                reply_markup=cinema_data_keyboard,
                                parse_mode="Markdown")
