import asyncio

from sqlalchemy import Integer, ForeignKey, String, Enum, Text
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship

connection = "postgresql+asyncpg://user:pass@localhost:5432/db_name"
engine = create_async_engine(connection)

async_session = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String)

    enrollments: Mapped[list["Enrollment"]] = relationship(
        "Enrollment",
        back_populates="user"
    )

    course_proxy = association_proxy("enrollments", "course")

class Course(Base):
    __tablename__ = "courses"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String)
    content: Mapped[str] = mapped_column(Text)

    enrollments: Mapped[list["Enrollment"]] = relationship(
        "Enrollment",
        back_populates="course"
    )

    user_proxy = association_proxy("enrollments", "user")

class Enrollment(Base):
    __tablename__ = "enrollments"

    role: Mapped[str] = mapped_column(Enum("Student", "Mentor"), name="role_enum")

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), primary_key=True)
    course_id: Mapped[int] = mapped_column(ForeignKey("courses.id"), primary_key=True)

    user: Mapped["User"] = relationship(
        "User",
        back_populates="enrollments"
    )

    course: Mapped["Course"] = relationship(
        "Course",
        back_populates="enrollments"
    )

async def create_user(username: str) -> User:
    async with async_session() as session:
        new_user = User(username=username)
        session.add(new_user)
        await session.commit()

        return new_user

async def create_course(title: str, content: str) -> Course:
    async with async_session() as session:
        new_course = Course(title=title, content=content)
        session.add(new_course)
        await session.commit()

        return new_course

async def init_db():
    async with engine.begin() as conn:
        conn.run_sync(Base.metadata.create_all)

async def main():
    await init_db()

if __name__ == "__main__":
    asyncio.run(main())