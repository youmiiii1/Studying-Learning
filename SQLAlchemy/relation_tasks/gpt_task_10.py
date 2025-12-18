from sqlalchemy import create_engine, ForeignKey, Integer, String, Text
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship

connection = "sqlite:///social_media.db"
engine = create_engine(connection)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "table_users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String)

    posts: Mapped[list["Post"]] = relationship(back_populates="user")

class Post(Base):
    __tablename__ = "table_posts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String)
    content: Mapped[str] = mapped_column(Text)
    user_id: Mapped[int] = mapped_column(ForeignKey("table_users.id"))

    user: Mapped["User"] = relationship(back_populates="posts")
    comments: Mapped[list["Comment"]] = relationship(back_populates="post")

class Comment(Base):
    __tablename__ = "table_comments"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    text: Mapped[str] = mapped_column(String)
    post_id: Mapped[int] = mapped_column(ForeignKey("table_posts.id"))
    post: Mapped["Post"] = relationship(back_populates="comments")

Base.metadata.create_all(engine)