import openai
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import dotenv_values
from jinja2 import Template

from src.packages.utils import LoadFile

bot = Bot(dotenv_values().get("API_KEY_TELEGRAM"))
openai.api_key = dotenv_values().get("API_KEY_OPENAI")
salutespeech_api_key = dotenv_values().get("API_KEY_SALUTESPEECH")
nasa_api_key = dotenv_values().get("API_KEY_NASA")
storage = MemoryStorage()
dispatcher = Dispatcher(bot, storage=storage)
load_text_messages = LoadFile().load_json("text_messages.json")
load_anime = LoadFile().load_json("anime.json")
load_cartoons = LoadFile().load_json("cartoons.json")
load_films = LoadFile().load_json("films.json")
load_serials = LoadFile().load_json("serials.json")
load_jokes = LoadFile().load_json("jokes.json")
template_json = Template
