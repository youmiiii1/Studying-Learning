""" Использование @hybrid_method + .expression -> 1 """

from sqlalchemy import create_engine, Float, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from sqlalchemy.ext.hybrid import hybrid_method


# --- Базовая модель ---
class Base(DeclarativeBase):
    pass


# --- Модель Product ---
class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    price: Mapped[float]
    discount: Mapped[float]

    @hybrid_method
    def price_with_discount(self):
        return self.price * (1 - self.discount)

    @price_with_discount.expression
    def price_with_discount(cls):
        return cls.price * (1 - cls.discount)


# --- Создание базы ---
engine = create_engine("sqlite:///:memory:")
Base.metadata.create_all(engine)

""" Использование @hybrid_method + .expression -> 2 """

from sqlalchemy import create_engine, String, select, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from sqlalchemy.ext.hybrid import hybrid_property


# --- Базовая модель ---
class Base(DeclarativeBase):
    pass


# --- Модель User ---
class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str]
    last_name: Mapped[str]

    @hybrid_property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @full_name.expression
    def full_name(cls):
        return cls.first_name + " " + cls.last_name


# --- Создание базы ---
engine = create_engine("sqlite:///:memory:")
Base.metadata.create_all(engine)

""" Использование @hybrid_method + .expression -> 3 """

from sqlalchemy import create_engine, DateTime, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime


# --- Базовая модель ---
class Base(DeclarativeBase):
    pass


# --- Модель Invoice ---
class Invoice(Base):
    __tablename__ = "invoices"

    id: Mapped[int] = mapped_column(primary_key=True)
    paid_at: Mapped[datetime | None]

    @hybrid_property
    def is_paid(self):
        return self.paid_at is not None

    @is_paid.expression
    def is_paid(cls):
        return cls.paid_at.isnot(None)


# --- Создание базы ---
engine = create_engine("sqlite:///:memory:")
Base.metadata.create_all(engine)

""" Использование @hybrid_method + .expression -> 4 """

from sqlalchemy import create_engine, String, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from sqlalchemy.ext.hybrid import hybrid_method


# --- Базовая модель ---
class Base(DeclarativeBase):
    pass


# --- Модель User ---
class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    role: Mapped[str] = mapped_column(String)

    @hybrid_method
    def has_role(self, role_name):
        return self.role == role_name

    @has_role.expression
    def has_role(cls, role_name):
        return cls.role == role_name


# --- Создание базы ---
engine = create_engine("sqlite:///:memory:")
Base.metadata.create_all(engine)

""" Использование @hybrid_method + .expression -> 5 """

from sqlalchemy import create_engine, Integer, Float, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from sqlalchemy.ext.hybrid import hybrid_property


# --- Модель ---
class Base(DeclarativeBase):
    pass


class OrderItem(Base):
    __tablename__ = "order_items"

    id: Mapped[int] = mapped_column(primary_key=True)
    price: Mapped[float]
    quantity: Mapped[int]

    @hybrid_property
    def total(self):
        return self.price * self.quantity

    @total.expression
    def total(cls):
        return cls.price * cls.quantity


# --- Создание базы ---
engine = create_engine("sqlite:///:memory:")
Base.metadata.create_all(engine)