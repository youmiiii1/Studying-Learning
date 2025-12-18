from sqlalchemy import create_engine, Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship, Session
from sqlalchemy.ext.associationproxy import association_proxy

engine = create_engine("sqlite:///shop.db")


class Base(DeclarativeBase):
    pass


class Customer(Base):
    __tablename__ = "customers"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)

    orders: Mapped[list["Order"]] = relationship("Order", back_populates="customer")


class Order(Base):
    __tablename__ = "orders"
    id: Mapped[int] = mapped_column(primary_key=True)

    customer_id: Mapped[int] = mapped_column(ForeignKey("customers.id"))
    customer: Mapped["Customer"] = relationship("Customer", back_populates="orders")

    items: Mapped[list["OrderItem"]] = relationship("OrderItem", back_populates="order")


class OrderItem(Base):
    __tablename__ = "order_items"
    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(String)
    price: Mapped[int] = mapped_column(Integer)

    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id"))
    order: Mapped["Order"] = relationship("Order", back_populates="items")


def get_customer_orders(customer_id):
    with Session(engine) as session:
        customer = session.get(Customer, customer_id)
        return [orders.id for orders in customer.orders]

def get_order_items(order_id):
    with Session(engine) as session:
        order = session.get(Order, order_id)
        return [order_item.name for order_item in order.items]

def get_customer_items(customer_id):
    with Session(engine) as session:
        customer = session.get(Customer, customer_id)
        return [item.name for order in customer.orders for item in order.items]

def get_customers_who_bought(item_name):
    with Session(engine) as session:
        customers = session.query(Customer).all()
        return [
            customer.name
            for customer in customers
            if any(item.name == item_name for order in customer.orders for item in order.items)
        ]


Base.metadata.create_all(engine)
