from aiogram import executor

from src.packages.bot import dispatcher


def main():
    executor.start_polling(dispatcher, skip_updates=True)


if __name__ == "__main__":
    main()
