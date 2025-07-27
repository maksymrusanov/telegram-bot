from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Integer
from sqlalchemy import create_engine
engine = create_engine("sqlite:///database/db.sqlite3", echo=True)


class Base(DeclarativeBase):
    pass


class Database(Base):
    __tablename__ = 'offers'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String)
    price: Mapped[int] = mapped_column(Integer)
    url: Mapped[str] = mapped_column(String)


Base.metadata.create_all(engine)
