from datetime import datetime

from gino import Gino
from sqlalchemy import Column, Integer, BigInteger, String, sql, DateTime

db = Gino()


class Users(db.Model):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(Integer())
    chat_id = Column(Integer())
    first_name = Column(String(50))
    last_name = Column(String(50))
    username = Column(String(50))
    date = Column(DateTime(), default=datetime.now())
    query = sql.select
