from .database import Database

database = Database()


async def setup_postgresql():
    await database.connect_db()
    await database.create_tables()
