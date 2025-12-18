from sqlalchemy import create_engine, Integer, String, ForeignKey, DateTime, text, Numeric, Text
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship
from datetime import datetime

connection = "sqlite:///kino.db"
engine = create_engine(connection)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "user_table"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String)

    posts: Mapped[list["Post"]] = relationship(
        "Post",
        back_populates="user"
    )

    comments: Mapped[list["Comment"]] = relationship(
        "Comment",
        back_populates="user"
    )

class Post(Base):
    __tablename__ = "post_table"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String)
    content: Mapped[str] = mapped_column(Text)

    user_id: Mapped[int] = mapped_column(ForeignKey("user_table.id"))

    user: Mapped["User"] = relationship(
        "User",
        back_populates="posts"
    )

    comments: Mapped[list["Comment"]] = relationship(
        "Comment",
        back_populates="post"
    )

    posts_tags: Mapped[list["PostTag"]] = relationship(
        "PostTag",
        back_populates="post"
    )

class Comment(Base):
    __tablename__ = "comment_table"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    content: Mapped[str] = mapped_column(Text)

    user_id: Mapped[int] = mapped_column(ForeignKey("user_table.id"))
    post_id: Mapped[int] = mapped_column(ForeignKey("post_table.id"))

    user: Mapped["User"] = relationship(
        "User",
        back_populates="comments"
    )

    post: Mapped["Post"] = relationship(
        "Post",
        back_populates="comments"
    )

class Tag(Base):
    __tablename__ = "tag_table"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)

    posts_tags: Mapped[list["PostTag"]] = relationship(
        "PostTag",
        back_populates="tag"
    )

class PostTag(Base):
    __tablename__ = "post_tag_table"

    post_id: Mapped[int] = mapped_column(ForeignKey("post_table.id"), primary_key=True)
    tag_id: Mapped[int] = mapped_column(ForeignKey("tag_table.id"), primary_key=True)

    tag: Mapped["Tag"] = relationship(
        "Tag",
        back_populates="posts_tags"
    )

    post: Mapped["Post"] = relationship(
        "Post",
        back_populates="posts_tags"
    )

Base.metadata.create_all(engine)
