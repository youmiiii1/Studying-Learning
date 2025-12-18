from sqlalchemy import create_engine, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.ext.associationproxy import association_proxy
from datetime import datetime

connection = "sqlite:///library.db"
engine = create_engine(connection)


class Base(DeclarativeBase):
    pass


class Author(Base):
    __tablename__ = "authors"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)

    # One-to-Many → автор → книги
    books: Mapped[list["Book"]] = relationship(back_populates="author")

    # Many-to-Many (через книги → borrows → readers)
    readers = association_proxy("books", "readers")


class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String)
    year: Mapped[int] = mapped_column(Integer)

    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"))

    # связь Many-to-One → многие книги у одного автора
    author: Mapped["Author"] = relationship(back_populates="books")

    # Borrow связь
    borrows: Mapped[list["Borrow"]] = relationship(back_populates="book")

    # связь Many-to-Many (через Borrow)
    readers = association_proxy("borrows", "reader")


class Reader(Base):
    __tablename__ = "readers"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)

    # Borrow связь
    borrows: Mapped[list["Borrow"]] = relationship(back_populates="reader")

    # связь Many-to-Many (через Borrow)
    books = association_proxy("borrows", "book")

    # связь Reader → Author (через books → author)
    authors = association_proxy("books", "author")


class Borrow(Base):
    __tablename__ = "borrows"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    taken_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    returned_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)

    reader_id: Mapped[int] = mapped_column(ForeignKey("readers.id"))
    book_id: Mapped[int] = mapped_column(ForeignKey("books.id"))

    # связь Borrow → Reader
    reader: Mapped["Reader"] = relationship(back_populates="borrows")

    # связь Borrow → Book
    book: Mapped["Book"] = relationship(back_populates="borrows")


Base.metadata.create_all(engine)
