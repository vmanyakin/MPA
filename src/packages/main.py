from aiogram import executor
from bot import dispatcher
from bot.utils import LoadFile


def main():
    executor.start_polling(dispatcher, skip_updates=True)


if __name__ == "__main__":
    main()
