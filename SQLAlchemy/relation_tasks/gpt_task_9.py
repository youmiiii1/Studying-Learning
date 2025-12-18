from sqlalchemy import create_engine, Integer, String, ForeignKey, DateTime, Numeric
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.ext.associationproxy import association_proxy
from datetime import datetime

connection = "sqlite:///library.db"
engine = create_engine(connection)

class Base(DeclarativeBase):
    pass

class Store(Base):
    __tablename__ = "table_store"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    address: Mapped[str] = mapped_column(String)

    orders: Mapped[list["Order"]] = relationship(back_populates="store")

class Order(Base):
    __tablename__ = "table_order"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    created_at: Mapped[datetime] = mapped_column(DateTime)
    store_id: Mapped[int] = mapped_column(ForeignKey("table_store.id"))

    store: Mapped["Store"] = relationship(back_populates="orders")
    order_items: Mapped[list["OrderItem"]] = relationship(back_populates="order")

class OrderItem(Base):
    __tablename__ = "table_orderitem"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    product_name: Mapped[str] = mapped_column(String)
    quantity: Mapped[int] = mapped_column(Integer)
    order_id: Mapped[int] = mapped_column(ForeignKey("table_order.id"))

    order: Mapped["Order"] = relationship(back_populates="order_items")

Base.metadata.create_all(engine)
