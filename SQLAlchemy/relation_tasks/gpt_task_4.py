from sqlalchemy import create_engine, Integer, String, Numeric, Enum, DateTime, CheckConstraint, select, update, delete, \
    text, UniqueConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from datetime import datetime

connection = "postgresql+psycopg2://postgres:postgres@localhost:5432/orders_db"

engine = create_engine(connection)

class Base(DeclarativeBase):
    pass

class Order(Base):
    __tablename__ = "orders_table"
    __table_args__ = (
        CheckConstraint("total >= 0", name="Total_positive"),
        UniqueConstraint("customer_name", "created_at", name="unique_customer_per_day")
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    customer_name: Mapped[str] = mapped_column(String(120), nullable=False)
    total: Mapped[float] = mapped_column(Numeric(10,2))
    status: Mapped[str] = mapped_column(Enum("new", "paid", "shipped", "canceled", name="order_status"))
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=text("CURRENT_TIMESTAMP"))

Base.metadata.create_all(engine)

def create_order(customer_name, total, status):
    with Session(engine) as session:
        new_order = Order(customer_name=customer_name, total=total, status=status)
        session.add(new_order)
        session.commit()

create_order("Michael", 1, "new")

def get_orders_by_status(status):
    with Session(engine) as session:
        stmt = select(Order).where(Order.status == status)
        result = session.scalars(stmt).all()
        return result

get_orders_by_status("new")

def get_orders_more_than(sum_value):
    with Session(engine) as session:
        stmt = select(Order).where(Order.total >= sum_value)
        result = session.scalars(stmt).all()
        return result

get_orders_more_than(50)

def update_order_status(order_id, new_status):
    with Session(engine) as session:
        stmt = (
            update(Order)
            .where(Order.id == order_id)
            .values(status=new_status)
        )
        session.execute(stmt)
        session.commit()

update_order_status(1, "paid")

def delete_canceled_orders():
    with Session(engine) as session:
        stmt = delete(Order).where(Order.status == "canceled")
        session.execute(stmt)
        session.commit()

delete_canceled_orders()




