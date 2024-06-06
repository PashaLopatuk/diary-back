from datetime import datetime

from sqlalchemy import DateTime, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.database.orm.models.base import Base


class Remembrance(Base):
    __tablename__ = 'remembrance'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    date: Mapped[datetime] = mapped_column(DateTime())
    title: Mapped[str] = mapped_column(String())
    description: Mapped[str] = mapped_column(String())
