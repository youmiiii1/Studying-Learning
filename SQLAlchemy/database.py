"""
1 - Step -> pip install sqlalchemy

Совет: Если вы работаете с PostgreSQL или MySQL, понадобится дополнительный драйвер:

PostgreSQL: pip install psycopg2-binary
MySQL: pip install pymysql

"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, DateTime
from datetime import datetime

connect_database = "postgresql+psycopg2://postgres:123456789@localhost:5432/sql_alchemy_test"

# Создание движка подключения к PostgreSQL
engine = create_engine(connect_database)

class Base(DeclarativeBase):
    pass

# Создание / инициализация таблицы и ее колонок
class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    age: Mapped[int] = mapped_column(Integer, nullable=False)
    time: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


# Base.metadata.create_all(engine)
