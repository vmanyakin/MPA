"""
Setting up commands for nasa
"""

import datetime
import random

import aiohttp
from aiogram import types
from aiogram.dispatcher import FSMContext

from src.packages.bot.keyboards import nasa_data_keyboard, nasa_start_keyboard, hello_keyboard
from src.packages.bot.loader import bot, dispatcher, load_text_messages, template_json, nasa_api_key
from src.packages.bot.states import NASA
from src.packages.database.mongodb import UsersCollection


async def random_data(start='2000-01-01'):
    start = datetime.date(*map(int, start.split('-')))
    end = datetime.date.today()
    delta = end - start
    result = str(start + datetime.timedelta(days=random.randint(0, delta.days)))
    return result


@dispatcher.callback_query_handler(text="NASA")
async def nasa_start(call: types.CallbackQuery, state: FSMContext):
    await UsersCollection.add(call.from_user.id, call.message.chat.id, call.from_user.first_name,
                              call.from_user.last_name, call.from_user.username, call.data)
    text_nasa_start = template_json(
        load_text_messages["nasa"]["nasa_start"] + load_text_messages["nasa"]["label"]).render()
    await NASA.query.set()
    await call.message.answer(text_nasa_start, reply_markup=nasa_start_keyboard)


@dispatcher.callback_query_handler(lambda x: x.data != "complete", state=NASA.query)
async def nasa_data(call: types.CallbackQuery | types.Message, state: FSMContext):
    nasa_data_except_answer = template_json(
        load_text_messages["nasa"]["nasa_data"]["nasa_data_except_answer"] + load_text_messages["nasa"][
            "label"]).render()
    nasa_data_except_query = template_json(
        load_text_messages["nasa"]["nasa_data"]["nasa_data_except_query"] + load_text_messages["label_MPA"]).render()
    text_label = template_json(load_text_messages["nasa"]["label"]).render()
    chat_id = call.message.chat.id
    try:
        async with aiohttp.ClientSession() as session:
            url = 'https://api.nasa.gov/planetary/apod'
            api_key = nasa_api_key
            date = await random_data()
            data = {'date': date, 'api_key': api_key}
            async with session.get(url, params=data) as resp:
                get_data = await resp.json()
                text = get_data["explanation"]
                if get_data["hdurl"]:
                    photo = get_data["hdurl"]
                else:
                    photo = get_data["url"]
        try:
            await bot.send_photo(chat_id=chat_id, photo=photo, caption=text + text_label,
                                 reply_markup=nasa_data_keyboard)
        except:
            await bot.send_message(chat_id=chat_id, text=nasa_data_except_answer, reply_markup=nasa_data_keyboard)
    except:
        await state.finish()
        await bot.send_message(chat_id=chat_id, text=nasa_data_except_query, reply_markup=hello_keyboard)


@dispatcher.message_handler(state=NASA.query)
@dispatcher.callback_query_handler(text="complete", state=NASA.query)
async def nasa_complete(call: types.CallbackQuery, state: FSMContext):
    chat_id = call.message.chat.id if isinstance(call, types.CallbackQuery) else call.chat.id
    text_nasa_complete = template_json(
        load_text_messages["nasa"]["nasa_complete"] + load_text_messages["label_MPA"]).render()
    await state.finish()
    await bot.send_message(chat_id=chat_id, text=text_nasa_complete, reply_markup=hello_keyboard)
