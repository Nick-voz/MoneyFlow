from base_model import BaseModel
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class User(BaseModel):
    __tablename__ = "users"
    id: Mapped[str] = mapped_column(primary_key=True)
    hiden_chat_id: Mapped[int]
    global_user_id: Mapped[str]
