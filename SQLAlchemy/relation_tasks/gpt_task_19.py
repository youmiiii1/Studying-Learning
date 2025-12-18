from sqlalchemy import create_engine, Integer, String, ForeignKey, DateTime, text, Numeric
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship
from datetime import datetime

connection = "sqlite:///kino.db"
engine = create_engine(connection)

class Base(DeclarativeBase):
    pass

# --- Пользователи ---
class User(Base):
    __tablename__ = "table_users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String)

    orders: Mapped[list["Order"]] = relationship(
        "Order",
        back_populates="user"
    )

# --- Товары ---
class Product(Base):
    __tablename__ = "table_products"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    price: Mapped[float] = mapped_column(Numeric(10,2))

    order_items: Mapped[list["OrderItem"]] = relationship(
        "OrderItem",
        back_populates="product"
    )

# --- Заказы ---
class Order(Base):
    __tablename__ = "table_orders"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    user_id: Mapped[int] = mapped_column(ForeignKey("table_users.id"))

    user: Mapped["User"] = relationship(
        "User",
        back_populates="orders"
    )

    order_items: Mapped[list["OrderItem"]] = relationship(
        "OrderItem",
        back_populates="order"
    )

# --- Ассоциативная таблица (Order ↔ Product) ---
class OrderItem(Base):
    __tablename__ = "table_order_items"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    quantity: Mapped[int] = mapped_column(Integer)

    order_id: Mapped[int] = mapped_column(ForeignKey("table_orders.id"))
    product_id: Mapped[int] = mapped_column(ForeignKey("table_products.id"))

    order: Mapped["Order"] = relationship(
        "Order",
        back_populates="order_items"
    )

    product: Mapped["Product"] = relationship(
        "Product",
        back_populates="order_items"
    )

Base.metadata.create_all(engine)
