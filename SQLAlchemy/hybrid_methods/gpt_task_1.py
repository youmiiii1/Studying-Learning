from sqlalchemy import create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.hybrid import hybrid_method, hybrid_property


class Base(DeclarativeBase):
    pass

class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)
    total: Mapped[float]
    tax: Mapped[float]

    @hybrid_property
    def total_with_tax(self):
        return self.total + (self.total * self.tax)

    @total_with_tax.expression
    def total_with_tax(cls):
        return cls.total + (cls.total * cls.tax)