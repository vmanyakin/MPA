from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import dotenv_values
from jinja2 import Template

from src.packages.utils import LoadFile

bot = Bot(dotenv_values().get("API_KEY_TELEGRAM"))
storage = MemoryStorage()
dispatcher = Dispatcher(bot, storage=storage)
load_json = LoadFile().load_text_messages()
template_json = Template

print(load_json)

