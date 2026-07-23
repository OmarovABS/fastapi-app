from sqlalchemy import String, Numeric
from sqlalchemy.orm import Mapped, mapped_column
from app.db import Base

class Dish(Base):
    __tablename__ = "dish"
    id : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(nullable=False)
    price: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False, default=0.00)
    category: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)