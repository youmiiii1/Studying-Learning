from sqlalchemy import create_engine, Integer, String, ForeignKey, Table
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session
from sqlalchemy.ext.associationproxy import association_proxy

engine = create_engine("sqlite:///library.db")

class Base(DeclarativeBase):
    pass

book_categories = Table(
    "book_categories",
    Base.metadata,
    mapped_column("book_id", ForeignKey("books.id"), primary_key=True),
    mapped_column("category_id", ForeignKey("categories.id"), primary_key=True)
)

borrowed = Table(
    "borrowed",
    Base.metadata,
    mapped_column("member_id", ForeignKey("members.id"), primary_key=True),
    mapped_column("book_id", ForeignKey("books.id"), primary_key=True)
)

class Author(Base):
    __tablename__ = "authors"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)

    books: Mapped[list["Book"]] = relationship("Book", back_populates="author")

class Book(Base):
    __tablename__ = "books"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String)

    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"))
    author: Mapped["Author"] = relationship("Author", back_populates="books")

    categories_rel: Mapped[list["Category"]] = relationship(
        "Category", secondary=book_categories, back_populates="books"
    )
    categories: Mapped[list[str]] = association_proxy("categories_rel", "name")

class Category(Base):
    __tablename__ = "categories"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)

    books: Mapped[list["Book"]] = relationship(
        "Book", secondary=book_categories, back_populates="categories_rel"
    )

class Member(Base):
    __tablename__ = "members"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)

    borrowed_books_rel: Mapped[list["Book"]] = relationship(
        "Book", secondary=borrowed
    )
    borrowed_books: Mapped[list[str]] = association_proxy("borrowed_books_rel", "title")

Base.metadata.create_all(engine)

def get_author_books(author_id):
    with Session(engine) as session:
        author = session.get(Author, author_id)
        return [book.title for book in author.books]

def get_book_categories(book_id):
    with Session(engine) as session:
        book = session.get(Book, book_id)
        return [category for category in book.categories]

def get_member_categories(member_id):
    with Session(engine) as session:
        member = session.get(Member, member_id)
        return [category.name for borrowed_book in member.borrowed_books_rel for category in borrowed_book.categories_rel]

def get_category_members(category_name):
    with Session(engine) as session:
        members = session.query(Member).all()
        return [
            member.name
            for member in members
            for book in member.borrowed_books_rel
            if any(category.name == category_name for category in book.categories_rel)
        ]