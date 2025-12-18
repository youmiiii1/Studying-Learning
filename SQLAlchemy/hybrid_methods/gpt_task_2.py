from sqlalchemy import create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.hybrid import hybrid_method

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    balance: Mapped[float]

    @hybrid_method
    def has_enough_money(self, amount):
        return self.balance >= amount

    @has_enough_money.expression
    def has_enough_money(cls, amount):
        return cls.balance >= amount