from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class FoodEntry(Base):
    __tablename__ = "food_entries"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )

    food_name: Mapped[str] = mapped_column(String(255))

    calories: Mapped[int] = mapped_column(Integer)
