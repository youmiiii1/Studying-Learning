from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy import String, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
import asyncio

class Base(DeclarativeBase):
    pass

connection = "postgresql+asyncpg://user:pass@localhost/dbname"
engine = create_async_engine(connection)

async_session = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)

async def create_user(name):
    async with async_session() as session:
        new_user = User(name=name)
        session.add(new_user)
        await session.commit()

async def get_user_by_name(name):
    async with async_session() as session:
        stmt = select(User).where(User.name == name)
        user = await session.scalars(stmt)
        return user.first()

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def main():
    await init_db()


asyncio.run(main())