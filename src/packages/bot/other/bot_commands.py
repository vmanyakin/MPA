"""
The help menu in the bot
"""

from aiogram.types import BotCommand

from src.packages.bot.loader import bot


async def setup_bot_commands(dispatcher):
    bot_commands = [
        BotCommand(command="/start", description="Описание возможностей"),
        BotCommand(command="/menu", description="Меню")
    ]
    await bot.set_my_commands(bot_commands)
