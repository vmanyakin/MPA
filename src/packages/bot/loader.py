from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import dotenv_values
from jinja2 import Template
import openai

from src.packages.utils import LoadFile

bot = Bot(dotenv_values().get("API_KEY_TELEGRAM"))
openai.api_key = dotenv_values().get("API_KEY_OPENAI")

storage = MemoryStorage()
dispatcher = Dispatcher(bot, storage=storage)
load_json = LoadFile().load_text_messages()
template_json = Template

