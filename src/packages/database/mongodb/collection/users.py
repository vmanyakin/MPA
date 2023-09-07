import logging
from datetime import datetime

from ..database import MongoDB
from ..schemes import Users


class UsersCollection:

    @staticmethod
    async def add(user_id: int, chat_id: int, first_name: str, last_name: str, username: str, name_module: str) -> int:
        """
        The method add an entry to the collection users
        """
        try:
            user = Users(user_id=user_id, chat_id=chat_id, first_name=first_name, last_name=last_name,
                         username=username, name_module=name_module, date=str(datetime.now())).get_data()
            await MongoDB.collection_users.insert_one(user)
        except Exception as exception:
            logging.error(f"MongoDB no data added to the UsersCollection: {exception}")
