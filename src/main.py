from aiogram import executor

from src.packages.bot import dispatcher
from src.packages.database.mongodb import setup_mongodb
from src.packages.database.postgresql import setup_postgresql


async def on_startup(dispatcher):
    await setup_postgresql()
    await setup_mongodb()


def main():
    executor.start_polling(dispatcher, skip_updates=True, on_startup=on_startup)


if __name__ == "__main__":
    main()
