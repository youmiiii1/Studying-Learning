from sqlalchemy import create_engine, Integer, String, Float, Boolean, DateTime, select, delete, CheckConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from datetime import datetime

connection = "postgresql+psycopg2://postgres:postgres@localhost:5432/shop"
engine = create_engine(connection)

class Base(DeclarativeBase):
    pass

class Product(Base):
    __tablename__ = "product_table"
    __table_args__ = (
        CheckConstraint("price > 0", name="positive_price"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(100), unique=True)
    price: Mapped[float] = mapped_column(Float)
    in_stock: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(engine)

def create_product(title, price, in_stock=True):
    with Session(engine) as session:
        new_product = Product(title=title, price=price, in_stock=in_stock)
        session.add(new_product)
        session.commit()

create_product("iPhone", 4500, in_stock=False)

def get_products_cheaper_than(limit_price):
    with Session(engine) as session:
        stmt = select(Product).where(Product.price < limit_price)
        products_result = session.scalars(stmt).all()
        return products_result

product_result = get_products_cheaper_than(9000)
for product in product_result:
    print(product.id, product.title, product.price)

def update_price(product_id, new_price):
    with Session(engine) as session:
        product_update = session.get(Product, product_id)
        if not product_update:
            return False
        product_update.price = new_price
        session.commit()
        return True

update_price(1, 2500)

def delete_not_in_stock():
    with Session(engine) as session:
        stmt = delete(Product).where(Product.in_stock == False)
        session.execute(stmt)
        session.commit()

delete_not_in_stock()




