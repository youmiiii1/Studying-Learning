from sqlalchemy import create_engine, Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship, Session
from sqlalchemy.ext.associationproxy import association_proxy

engine = create_engine("sqlite:///blog.db")

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)

    posts_rel: Mapped[list["Post"]] = relationship("Post", back_populates="author")
    posts: Mapped[list[str]] = association_proxy("posts_rel", "title")


class Post(Base):
    __tablename__ = "posts"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String)
    body: Mapped[str] = mapped_column(String)

    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    author: Mapped["User"] = relationship("User", back_populates="posts_rel")

    comments_rel: Mapped[list["Comment"]] = relationship("Comment", back_populates="post")
    comments: Mapped[list[str]] = association_proxy("comments_rel", "text")


class Comment(Base):
    __tablename__ = "comments"
    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column(String)

    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id"))
    post: Mapped["Post"] = relationship("Post", back_populates="comments_rel")

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship("User")

def get_user_posts(user_id):
    with Session(engine) as session:
        user = session.get(User, user_id)
        return user.posts

def get_post_comments(post_id):
    with Session(engine) as session:
        post = session.get(Post, post_id)
        return post.comments

def get_user_commented_posts(user_id):
    with Session(engine) as session:
        user = session.get(User, user_id)
        return [post.title for post in user.posts_rel for comment in post.comments_rel if comment.user_id == user_id]

def get_post_commenters(post_id):
    with Session(engine) as session:
        post = session.query(Post).filter_by(id = post_id).first()
        return [comment.user.name for comment in post.comments_rel]

Base.metadata.create_all(engine)
