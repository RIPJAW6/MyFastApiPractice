from sqlalchemy.orm import Mapped
from src.database import Base

class BookModel(Base):
    title: Mapped[str]
    description: Mapped[str | None]