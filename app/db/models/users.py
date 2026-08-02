from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db import Base

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False)
    telephone: Mapped[str] = mapped_column(nullable=False, unique=True)
    orders: Mapped[list["Order"]] = relationship(back_populates="user", cascade="all, delete-orphan")