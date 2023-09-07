import logging
from datetime import datetime

from asyncpg import UniqueViolationError

from ..schemes import Users


class UsersTable:
    """
    This class is to operate with database users table
    """

    @staticmethod
    async def add(user_id: int, chat_id: int, first_name: str, last_name: str, username: str) -> int:
        """
        The method adding a record to table users
        """
        try:
            user = Users(user_id=user_id, chat_id=chat_id, first_name=first_name, last_name=last_name,
                         username=username, date=datetime.now())
            await user.create()
        except UniqueViolationError as exception:
            logging.error(f"PostgreSQL no data added to the UsersTable: {exception}")
        except Exception as exception:
            logging.error(f"PostgreSQL no data added to the UsersTable: {exception}")
