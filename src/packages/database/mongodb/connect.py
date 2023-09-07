from .database import MongoDB


async def setup_mongodb():
    MongoDB().connection_setup()
