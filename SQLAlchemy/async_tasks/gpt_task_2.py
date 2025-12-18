import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, selectinload
from sqlalchemy import Integer, String, Boolean, Text, ForeignKey, select, update

connection = "postgresql+asyncpg://user:pass@localhost:5432/db_name"
engine = create_async_engine(connection)

async_session = async_sessionmaker(
    engine,
    class_= AsyncSession,
    expire_on_commit=False
)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "table_users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String, unique=True)
    is_active: Mapped[bool] = mapped_column(Boolean)

    posts: Mapped[list["Post"]] = relationship(
        "Post",
        back_populates="user",
        cascade="all, delete-orphan"
    )

class Post(Base):
    __tablename__ = "table_posts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String)
    content: Mapped[str] = mapped_column(Text)

    author_id: Mapped[int] = mapped_column(ForeignKey("table_users.id"))
    user: Mapped["User"] = relationship(
        "User",
        back_populates="posts"
    )

async def create_user(user_name: str) -> User:
    async with async_session() as session:
        new_user = User(username=user_name)
        session.add(new_user)
        await session.commit()
        return new_user

async def create_post(user_id: int, title: str, content: str) -> Post:
    async with async_session() as session:
        new_post = Post(author_id=user_id, title=title, content=content)
        session.add(new_post)
        await session.commit()
        return new_post

async def get_user_with_posts(username: str):
    async with async_session() as session:
        stmt = (
            select(User)
            .options(selectinload(User.posts))
            .where(User.username == username)
        )
        user = await session.scalars(stmt)
        return user.first()

async def update_post_title(post_id: int, new_title: str) -> None:
    async with async_session() as session:
        stmt = (
            update(Post)
            .where(Post.id == post_id)
            .values(title=new_title)
        )

        await session.execute(stmt)
        await session.commit()

async def delete_user(user_id: int) -> None:
    async with async_session() as session:
        user = await session.get(User, user_id)
        if user:
            await session.delete(user)
            await session.commit()

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def main():
    await init_db()

if __name__ == "__main__":
    asyncio.run(main())