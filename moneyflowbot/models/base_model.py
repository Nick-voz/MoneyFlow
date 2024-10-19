from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase

from utils.utils import get_db_url

engine = create_engine(get_db_url())


class BaseModel(DeclarativeBase):
    pass
