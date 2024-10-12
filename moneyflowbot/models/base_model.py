from os import getenv

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase


def get_db_url() -> str:
    DB_URL = getenv("DB_URL")
    if DB_URL is None:
        raise RuntimeError("can't load DB_URL")
    return DB_URL


load_dotenv()
engine = create_engine(get_db_url())


class BaseModel(DeclarativeBase):
    pass
