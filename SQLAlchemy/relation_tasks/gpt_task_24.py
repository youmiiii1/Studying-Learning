from sqlalchemy import create_engine, Integer, String, ForeignKey, Table
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship, Session
from sqlalchemy.ext.associationproxy import association_proxy

engine = create_engine("sqlite:///social.db")

class Base(DeclarativeBase):
    pass

# many-to-many посты ↔ лайки пользователей
post_likes = Table(
    "post_likes",
    Base.metadata,
    mapped_column("post_id", ForeignKey("posts.id"), primary_key=True),
    mapped_column("user_id", ForeignKey("users.id"), primary_key=True)
)

# many-to-many посты ↔ теги
post_tags = Table(
    "post_tags",
    Base.metadata,
    mapped_column("post_id", ForeignKey("posts.id"), primary_key=True),
    mapped_column("tag_id", ForeignKey("tags.id"), primary_key=True)
)

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)

    profile: Mapped["Profile"] = relationship("Profile", back_populates="user", uselist=False)
    posts: Mapped[list["Post"]] = relationship("Post", back_populates="author")
    liked_posts: Mapped[list["Post"]] = relationship("Post", secondary=post_likes, back_populates="liked_by_rel")

class Profile(Base):
    __tablename__ = "profiles"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    bio: Mapped[str] = mapped_column(String)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship("User", back_populates="profile")

class Post(Base):
    __tablename__ = "posts"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String)

    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    author: Mapped["User"] = relationship("User", back_populates="posts")

    liked_by_rel: Mapped[list["User"]] = relationship("User", secondary=post_likes, back_populates="liked_posts")
    liked_by: Mapped[list[str]] = association_proxy("liked_by_rel", "name")  # shortcut: имена пользователей

    tags_rel: Mapped[list["Tag"]] = relationship("Tag", secondary=post_tags, back_populates="posts")
    tags: Mapped[list[str]] = association_proxy("tags_rel", "name")  # shortcut: названия тегов

class Tag(Base):
    __tablename__ = "tags"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)

    posts: Mapped[list["Post"]] = relationship("Post", secondary=post_tags, back_populates="tags_rel")

Base.metadata.create_all(engine)

def get_user_posts(user_id):
    with Session(engine) as session:
        user = session.get(User, user_id)
        return [post.title for post in user.posts]

def get_post_likers(post_id):
    with Session(engine) as session:
        post = session.get(Post, post_id)
        return post.liked_by

def get_user_tags(user_id):
    with Session(engine) as session:
        user = session.get(User, user_id)
        return [tag.name for post in user.posts for tag in post.tags_rel]

def get_tag_posts(tag_name):
    with Session(engine) as session:
        tag = session.query(Tag).filter_by(name=tag_name).first()
        return [post.title for post in tag.posts]
