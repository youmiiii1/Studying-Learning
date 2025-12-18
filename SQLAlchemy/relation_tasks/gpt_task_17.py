from sqlalchemy import create_engine, Integer, String, ForeignKey, Numeric, Enum, DateTime, text
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship
from datetime import datetime

connection = "sqlite:///kino.db"
engine = create_engine(connection)

class Base(DeclarativeBase):
    pass

class Product(Base):
    __tablename__ = "table_products"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    price: Mapped[float] = mapped_column(Numeric(10,2))

    supply: Mapped[list["Supply"]] = relationship(
        "Supply",
        back_populates="product",
    )

class Supplier(Base):
    __tablename__ = "table_supplier"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    country: Mapped[str] = mapped_column(String)

    supply: Mapped[list["Supply"]] = relationship(
        "Supply",
        back_populates="supplier",
    )

class WareHouse(Base):
    __tablename__ = "table_warehouse"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    location: Mapped[str] = mapped_column(String)

    supply: Mapped[list["Supply"]] = relationship(
        "Supply",
        back_populates="warehouse",
    )

class Supply(Base):
    __tablename__ = "table_supply"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    delivered_at: Mapped[datetime] = mapped_column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    quantity: Mapped[int] = mapped_column(Integer)

    product_id: Mapped[int] = mapped_column(ForeignKey("table_products.id"))
    supplier_id: Mapped[int] = mapped_column(ForeignKey("table_supplier.id"))
    warehouse_id: Mapped[int] = mapped_column(ForeignKey("table_warehouse.id"))

    product: Mapped["Product"] = relationship("Product",back_populates="supply")
    supplier: Mapped["Supplier"] = relationship("Supplier",back_populates="supply")
    warehouse: Mapped["WareHouse"] = relationship("WareHouse",back_populates="supply")

Base.metadata.create_all(engine)


