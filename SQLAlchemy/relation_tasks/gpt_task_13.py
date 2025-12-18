from sqlalchemy import create_engine, ForeignKey, Integer, String, Text, DateTime
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship
from datetime import datetime

connection = "sqlite:///social_media.db"
engine = create_engine(connection)

class Base(DeclarativeBase):
    pass

class Author(Base):
    __tablename__ = "table_authors"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)

    books: Mapped[list["Book"]] = relationship(
        "Book",
        back_populates="authors",
        secondary="table_book_author"
    )

    books_assoc: Mapped[list["BookAuthor"]] = relationship("BookAuthor", back_populates="author")

class Book(Base):
    __tablename__ = "table_books"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String)

    authors: Mapped[list["Author"]] = relationship(
        "Author",
        back_populates="books",
        secondary="table_book_author"
    )

    authors_assoc: Mapped[list["BookAuthor"]] = relationship("BookAuthor", back_populates="book")

class BookAuthor(Base):
    __tablename__ = "table_book_author"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    published_at: Mapped[datetime] = mapped_column(DateTime, server_default="CURRENT_TIMESTAMP")
    book_id: Mapped[int] = mapped_column(ForeignKey("table_books.id"))
    author_id: Mapped[int] = mapped_column(ForeignKey("table_authors.id"))

    author: Mapped["Author"] = relationship(back_populates="books_assoc")
    book: Mapped["Book"] = relationship(back_populates="authors_assoc")

Base.metadata.create_all(engine)