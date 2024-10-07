from uuid import uuid4

from models.base_model import engine
from sqlalchemy import Select
from sqlalchemy.orm import Session

from moneyflowbot.models.user import User


def genertate_global_user_id() -> str:
    return str(uuid4())


def save_user(chat_id: int, global_user_id: str):
    user = User()
    user.hiden_chat_id = hide_chat_id(chat_id)
    user.global_user_id = global_user_id
    with Session(engine) as session:
        session.add(user)


def hide_chat_id(chat_id: int):
    return hash(str(chat_id))


def get_global_user_id(chat_id: int) -> str:
    hiden_chad_id = hide_chat_id(chat_id)
    selector = Select(User).where(User.hiden_chat_id == hiden_chad_id)
    with Session(engine) as session:
        user: User = session.scalars(selector).one()

    return user.global_user_id
