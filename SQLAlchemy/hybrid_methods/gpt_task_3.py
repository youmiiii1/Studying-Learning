from sqlalchemy import select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method

class Base(DeclarativeBase):
    pass

class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    price: Mapped[float]
    discount: Mapped[float]

    @hybrid_method
    def is_expensive(self, threshold):
        return self.price * (1 - self.discount) >= threshold

    @is_expensive.expression
    def is_expensive(cls, threshold):
        return cls.price * (1 - cls.discount) >= threshold

