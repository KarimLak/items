from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import Mapped, declarative_base, mapped_column

Base = declarative_base()

class Item(Base):
    __tablename__ = 'products'

    id : Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name : Mapped[str] = mapped_column(String(255), nullable=False)
    description : Mapped[str] = mapped_column(String, nullable=False)
    price : Mapped[float] = mapped_column(Float, nullable=False)
