import asyncio
import io
import urllib.parse
import uuid

import aiohttp
from aiogram import types
from pydub import AudioSegment

from src.packages.bot.loader import dispatcher, load_json, template_json, salutespeech_api_key


def blocking_io(oga_format):
    mp3 = AudioSegment.from_file(oga_format).export(io.BytesIO(), format="mp3")
    return mp3.read()


@dispatcher.callback_query_handler(text="SaluteSpeech")
async def salutespeech_start(call: types.CallbackQuery):
    text_salutespeech_start = template_json(
        load_json["salutespeech"]["salutespeech_start"] + load_json["salutespeech"]["label"]).render()
    await call.message.answer(text_salutespeech_start)


@dispatcher.message_handler(content_types=types.ContentType.VOICE)
async def salutespeech_start_translate_voice_in_text(message: types.Message):
    file_in_io = io.BytesIO()
    await message.voice.download(destination_file=file_in_io)
    oga_in_mp3 = asyncio.to_thread(blocking_io, file_in_io)
    bin_mp3 = await oga_in_mp3

    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
        oauth_url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"
        api_key = salutespeech_api_key
        headers_oauth = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/x-www-form-urlencoded",
            "RqUID": str(uuid.uuid4())
        }
        data_oauth = {
            "scope": "SALUTE_SPEECH_PERS"
        }
        encoded_data = urllib.parse.urlencode(data_oauth)
        async with session.post(oauth_url, data=encoded_data, headers=headers_oauth) as resp:
            get_data = await resp.json()
            access_token = get_data["access_token"]

    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
        url_api = "https://smartspeech.sber.ru/rest/v1/speech:recognize"
        headers_api = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "audio/mpeg"
        }
        async with session.post(url_api, data=bin_mp3, headers=headers_api) as resp:
            get_data = await resp.json()
            voice_to_text = " ".join(get_data["result"])
    text_label = template_json(load_json["salutespeech"]["label"]).render()
    await message.answer(voice_to_text + text_label)
