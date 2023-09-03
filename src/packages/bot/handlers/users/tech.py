from aiogram import types
from aiogram.dispatcher import FSMContext

from src.packages.bot.keyboards import tech_start_keyboard, tech_menu_keyboard, hello_keyboard
from src.packages.bot.loader import dispatcher, load_text_messages, template_json
from src.packages.bot.states import Tech


@dispatcher.callback_query_handler(text="Тех")
async def tech_start(call: types.CallbackQuery):
    text_tech_start = template_json(
        load_text_messages["tech"]["tech_start"] + load_text_messages["tech"]["label"]).render()
    await call.message.answer(text_tech_start, reply_markup=tech_start_keyboard)


@dispatcher.callback_query_handler(text="id")
async def tech_id(call: types.CallbackQuery):
    text_label = template_json(load_text_messages["tech"]["label"]).render()
    await call.message.answer(str(call.from_user.id) + text_label, reply_markup=tech_menu_keyboard)


@dispatcher.callback_query_handler(text="sticker")
async def tech_sticker(call: types.CallbackQuery):
    text_tech_sticker = template_json(
        load_text_messages["tech"]["tech_sticker"] + load_text_messages["tech"]["label"]).render()
    await call.message.answer(text_tech_sticker)
    await Tech.sticker.set()


@dispatcher.message_handler(content_types=[types.ContentType.STICKER, types.ContentType.TEXT], state=Tech.sticker)
async def tech_send_sticker(message: types.Message, state: FSMContext):
    text_label = template_json(load_text_messages["tech"]["label"]).render()
    text_tech_sticker_error = template_json(
        load_text_messages["tech"]["tech_sticker_error"] + load_text_messages["tech"]["label"]).render()
    if message.sticker:
        await state.finish()
        await message.answer(message.sticker.file_id + text_label, reply_markup=tech_menu_keyboard)
    else:
        await message.answer(text_tech_sticker_error, reply_markup=tech_menu_keyboard)


@dispatcher.callback_query_handler(text="menu", state=Tech.sticker)
async def tech_send_sticker(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    text_tech_sticker_complete = template_json(
        load_text_messages["tech"]["tech_sticker_complete"] + load_text_messages["label_MPA"]).render()
    await call.message.answer(text_tech_sticker_complete, reply_markup=hello_keyboard)
