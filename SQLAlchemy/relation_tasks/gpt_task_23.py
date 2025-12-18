from sqlalchemy import create_engine, Integer, ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship, Session

connection = "sqlite:///library.db"
engine = create_engine(connection)

class Base(DeclarativeBase):
    pass

class Author(Base):
    __tablename__ = "table_authors"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    books: Mapped[list["Book"]] = relationship(
        "Book",
        back_populates="author"
    )

class Book(Base):
    __tablename__ = "table_books"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)

    author_id: Mapped[int] = ForeignKey("table_authors.id")
    author: Mapped["Author"] = relationship(
        "Author",
        back_populates="books"
    )

    reviews: Mapped[list["Review"]] = relationship(
        "Review",
        back_populates="book"
    )

class Review(Base):
    __tablename__ = "table_reviews"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    book_id: Mapped[int] = mapped_column(ForeignKey("table_books.id"))
    book: Mapped["Book"] = relationship(
        "Book",
        back_populates="reviews"
    )

def global_session():
        return Session(engine)
global_session()

def get_author_books(session, author_id):
    author = session.get(Author, author_id)
    return [book.name for book in author.books]

def get_book_reviews(session, book_id):
    book = session.get(Book, book_id)
    return [review.id for review in book.reviews]

def get_author_reviews(session, author_id):
    author = session.get(Author, author_id)
    return [review for book in author.books for review in book.reviews]


Base.metadata.create_all(engine)