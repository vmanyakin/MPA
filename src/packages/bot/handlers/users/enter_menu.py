from src.packages.bot.loader import dispatcher, types


@dispatcher.message_handler()
async def hello(message:types.Message):
    await message.answer("Привет")