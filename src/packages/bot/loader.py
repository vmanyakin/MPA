from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import dotenv_values


bot = Bot(dotenv_values().get("API_KEY_TELEGRAM"))
storage = MemoryStorage()
dispatcher = Dispatcher(bot, storage=storage)
