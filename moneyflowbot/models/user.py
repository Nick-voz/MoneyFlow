from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from models.base_model import BaseModel
from models.base_model import engine


class User(BaseModel):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    chat_id: Mapped[int] = mapped_column(unique=True)
    global_user_id: Mapped[str]


BaseModel.metadata.create_all(engine)
