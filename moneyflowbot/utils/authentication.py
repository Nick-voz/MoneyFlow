from uuid import uuid4

from models.base_model import engine
from models.user import User
from sqlalchemy import Select
from sqlalchemy.orm import Session


def genertate_global_user_id() -> str:
    return str(uuid4())


# TODO: move this to user model
def save_user(chat_id: int, key: str):
    user = User()
    user.chat_id = chat_id
    user.global_user_id = str(hash(key))
    with Session(engine) as session:
        session.add(user)
        session.commit()


# TODO: move this to user model
def get_global_user_id(chat_id: int) -> str:
    selector = Select(User).where(User.chat_id == chat_id)
    with Session(engine) as session:
        user: User = session.scalars(selector).one()
    return user.global_user_id


# TODO: move this to user model
def delete_user(chat_id: int):
    selector = Select(User).where(User.chat_id == chat_id)
    with Session(engine) as session:
        user: User = session.scalars(selector).one()
        session.delete(user)
        session.commit()


def save_spend(): ...
