from aiogram.dispatcher.filters.state import StatesGroup, State


class ChatGPT(StatesGroup):

    prompt = State()