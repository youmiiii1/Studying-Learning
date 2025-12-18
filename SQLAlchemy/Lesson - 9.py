""" Использование метода __repr__ """

from sqlalchemy import create_engine, String, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

# --- Базовая модель ---
class Base(DeclarativeBase):
    pass

# --- Модель Book ---
class Book(Base):
    __tablename__ = "books"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String)

    # опишите метод __repr__
    def __repr__(self):
        return f"<Book id={self.id} title={self.title}>"

# --- Создание базы и данных ---
engine = create_engine("sqlite:///:memory:")
Base.metadata.create_all(engine)

from sqlalchemy import create_engine, String, Boolean, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session


# --- Базовая модель ---
class Base(DeclarativeBase):
    pass

""" Использование метода __init__ """

# --- Модель Employee ---
class Employee(Base):
    __tablename__ = "employees"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)
    manager: Mapped[bool] = mapped_column(Boolean)

    # опишите метод __init__
    def __init__(self, name: str, manager: bool = False):
        self.name = name
        self.manager = manager

""" Использование декоратора @property """

# --- Создание базы и данных ---
engine = create_engine("sqlite:///:memory:")
Base.metadata.create_all(engine)

from sqlalchemy import create_engine, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

# --- Базовая модель ---
class Base(DeclarativeBase):
    pass

# --- Модель Book ---
class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String)
    subtitle: Mapped[str | None] = mapped_column(String, nullable=True)

    # опишите вычисляемое поле
    @property
    def full_title(self):
        if not self.subtitle:
             return f"{self.title}"
        return f"{self.title}: {self.subtitle}"

# --- База и данные ---
engine = create_engine("sqlite:///:memory:")
Base.metadata.create_all(engine)

""" Использование декоратора @func_name.setter """

from sqlalchemy import create_engine, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session


# --- Базовая модель ---
class Base(DeclarativeBase):
    pass


# --- Модель Book ---
class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String)
    subtitle: Mapped[str | None] = mapped_column(String, nullable=True)

    # свойство full_title
    @property
    def full_title(self):
        return f"{self.title}: {self.subtitle}"

    # setter для full_title
    @full_title.setter
    def full_title(self, value: str):
        parts = value.split(":", 1)
        self.title = parts[0].strip()
        self.subtitle = parts[1].strip() if len(parts) > 1 else None


# --- Создание базы ---
engine = create_engine("sqlite:///:memory:")
Base.metadata.create_all(engine)

""" Использование декоратора @validate """

from sqlalchemy import create_engine, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, validates, Session


# --- Базовая модель ---
class Base(DeclarativeBase):
    pass


# --- Модель Book ---
class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String)
    pages: Mapped[int] = mapped_column(Integer)

    # валидация поля pages
    @validates("pages")
    def validate_pages(self, key, value):
        if value <= 0:
            raise ValueError("Число страниц должно быть положительным")
        return value


# --- База ---
engine = create_engine("sqlite:///:memory:")
Base.metadata.create_all(engine)
