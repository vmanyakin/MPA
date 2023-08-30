from aiogram.dispatcher.filters.state import StatesGroup, State


class NASA(StatesGroup):
    query = State()
