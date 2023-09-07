"""
Setting up commands for chatgpt
"""
import openai
from aiogram import types
from aiogram.dispatcher import FSMContext

from src.packages.bot.keyboards import chat_dialog_keyboard, hello_keyboard, chat_complete_keyboard
from src.packages.bot.loader import bot, dispatcher, load_text_messages, template_json
from src.packages.bot.states import ChatGPT
from src.packages.database.mongodb import UsersCollection


@dispatcher.callback_query_handler(text="ChatGPT")
async def chat_start(call: types.CallbackQuery, state: FSMContext):
    await UsersCollection.add(call.from_user.id, call.message.chat.id, call.from_user.first_name,
                              call.from_user.last_name, call.from_user.username, call.data)
    text_chat_start = template_json(
        load_text_messages["chat_gpt"]["chat_start"] + load_text_messages["chat_gpt"]["label"]).render()
    async with state.proxy() as data:
        data['model'] = "gpt-3.5-turbo"
        data['message'] = []
    await call.message.answer(text_chat_start)
    await ChatGPT.prompt.set()


@dispatcher.message_handler(state=ChatGPT.prompt)
async def chat_dialog(message: types.Message, state: FSMContext):
    text_chat_waiting = template_json(
        load_text_messages["chat_gpt"]["chat_dialog"]["chat_waiting"] + load_text_messages["chat_gpt"][
            "label"]).render()
    text_chat_except = template_json(
        load_text_messages["chat_gpt"]["chat_dialog"]["chat_except"] + load_text_messages["label_MPA"]).render()
    text_label = template_json(load_text_messages["chat_gpt"]["label"]).render()
    async with state.proxy() as data:
        data["message"].append({"role": "user", "content": message.text})
    bot_message = await bot.send_message(chat_id=message.chat.id, text=text_chat_waiting)
    try:
        gpt_request = await openai.ChatCompletion.acreate(
            model=data['model'],
            messages=data['message']
        )
        gpt_answer = gpt_request.choices[0].message.content
        async with state.proxy() as data:
            data["message"].append({"role": "assistant", "content": gpt_answer})
        await bot.edit_message_text(gpt_answer + text_label, chat_id=bot_message.chat.id,
                                    message_id=bot_message.message_id,
                                    reply_markup=chat_dialog_keyboard)
    except:
        await state.finish()
        await bot.edit_message_text(text_chat_except, chat_id=bot_message.chat.id,
                                    message_id=bot_message.message_id,
                                    reply_markup=hello_keyboard
                                    )


@dispatcher.callback_query_handler(text="reset", state=ChatGPT.prompt)
async def chat_reset(call: types.CallbackQuery, state: FSMContext):
    text_chat_reset = template_json(
        load_text_messages["chat_gpt"]["chat_reset"] + load_text_messages["chat_gpt"]["label"]).render()
    async with state.proxy() as data:
        data["message"].clear()
    await call.message.answer(text_chat_reset, reply_markup=chat_complete_keyboard)


@dispatcher.callback_query_handler(text="complete", state=ChatGPT.prompt)
async def chat_complete(call: types.CallbackQuery, state: FSMContext):
    text_chat_complete = template_json(
        load_text_messages["chat_gpt"]["chat_complete"] + load_text_messages["label_MPA"]).render()
    await state.finish()
    await call.message.answer(text_chat_complete, reply_markup=hello_keyboard)
