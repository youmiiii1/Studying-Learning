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

    products_proxy = association_proxy("items", "product")


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)

    items: Mapped[list["OrderItem"]] = relationship("OrderItem", back_populates="product")


class OrderItem(Base):
    __tablename__ = "order_items"

    id: Mapped[int] = mapped_column(primary_key=True)

    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id"))
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
    quantity: Mapped[int] = mapped_column(Integer)

    order: Mapped["Order"] = relationship("Order", back_populates="items")
    product: Mapped["Product"] = relationship("Product", back_populates="items")


Base.metadata.create_all(engine)

def get_customer_orders(session, customer_id):
    customer = session.get(Customer, customer_id)
    return [order.id for order in customer.orders]

def get_order_products(session, order_id):
    order = session.get(Order, order_id)
    return [product.name for product in order.products_proxy]

def get_customer_products(session, customer_id):
    customer = session.get(Customer, customer_id)
    return [product.name for order in customer.orders for product in order.products_proxy]

def get_order_product_quantities(session, order_id):
    order = session.get(Order, order_id)
    return [
        (a.product.name, a.quantity)
        for a in order.items
        ]

def get_customers_who_bought_product(session, product_name):
    product = session.query(Product).filter_by(name=product_name).first()
    return [order_item.order.customer.name for order_item in product.items]



