import logging
import os

import dotenv

from .schemes import db

dotenv.load_dotenv()


class Database:
    """
    Database class.The class contains the necessary
    methods for working with the postgres sql database.
    """

    def __init__(self):
        self.user = os.getenv("PG_USER")
        self.password = os.getenv("PG_PASSWORD")
        self.host = os.getenv("PG_HOST")
        self.port = os.getenv("PG_PORT")
        self.db_name = os.getenv("PG_DB_NAME")

    async def connect_db(self):
        """
        Method to connect to postgres database
        """
        try:
            await db.set_bind(
                f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.db_name}"
            )
        except Exception as exception:
            logging.error(f"PostgreSQL no connection: {exception}")

    @staticmethod
    async def __drop_tables():
        try:
            await db.gino.drop_all()
        except Exception as exception:
            logging.error(f"PostgreSQL not drop table: {exception}")

    @staticmethod
    async def create_tables():
        try:
            await db.gino.create_all()
        except Exception as exception:
            logging.error(f"PostgreSQL not create table: {exception}")
