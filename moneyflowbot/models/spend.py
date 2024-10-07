from sqlalchemy import Date
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from moneyflowbot.models.base_model import BaseModel


class Spend(BaseModel):
    __tablename__ = "spends"
    title: Mapped[str] = mapped_column(String(50))
    amount: Mapped[float]
    date: Mapped[Date] = mapped_column(Date)
