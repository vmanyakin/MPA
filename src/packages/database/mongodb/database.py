import logging
import os

import dotenv
import motor.motor_asyncio

dotenv.load_dotenv()


class MongoDB:
    """
    MongoDB class.The class contains the necessary
    methods for working with database.
    """

    MONGO_HOST = os.getenv("MONGO_HOST")
    MONGO_PORT = os.getenv("MONGO_PORT")
    MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")
    MONGO_USER = os.getenv("MONGO_USER")
    MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
    client = None
    db = None
    collection_users = None

    @classmethod
    def connection_setup(cls):
        try:
            cls.client = motor.motor_asyncio.AsyncIOMotorClient(f"mongodb://{cls.MONGO_HOST}:{cls.MONGO_PORT}")
            cls.db = cls.client.MPA
            cls.collection_users = cls.db.users
        except Exception as exception:
            logging.error(f"MongoDB no connection: {exception}")
