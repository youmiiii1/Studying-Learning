import asyncio
from sqlalchemy import Integer, String, Boolean, text, DATETIME, ForeignKey, select
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship, selectinload
from datetime import datetime

class Base(DeclarativeBase):
    pass

connection = "postgresql+asyncpg://name:pass@localhost:5432/db_name"
engine = create_async_engine(connection)

async_session = async_sessionmaker(
    engine,
    class_= AsyncSession,
    expire_on_commit= False
)

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String, unique=True)
    is_active: Mapped[bool] = mapped_column(Boolean)
    created_at: Mapped[datetime] = mapped_column(DATETIME, server_default=text("CURRENT_TIMESTAMP"))

    courses: Mapped[list["Course"]] = relationship(
        "Course",
        back_populates="author"
    )

    course_student: Mapped[list["CourseStudent"]] = relationship(
        "CourseStudent",
        back_populates="user"
    )

    course_titles = association_proxy("courses", "title")

class Course(Base):
    __tablename__ = "courses"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    is_published: Mapped[bool] = mapped_column(Boolean)

    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    author: Mapped["User"]= relationship(
        "User",
        back_populates="courses"
    )

    lessons: Mapped[list["Lesson"]] = relationship(
        "Lesson",
        back_populates="course"
    )

    course_student: Mapped[list["CourseStudent"]] = relationship(
        "CourseStudent",
        back_populates="course"
    )

    student_emails = association_proxy("author", "email")

class Lesson(Base):
    __tablename__ = "lessons"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String)
    content: Mapped[str] = mapped_column(String)
    order: Mapped[int] = mapped_column(Integer)

    course_id: Mapped[int] = mapped_column(ForeignKey("courses.id"))

    course: Mapped["Course"] = relationship(
        "Course",
        back_populates="lessons"
    )


class CourseStudent(Base):
    __tablename__ = "course_student"

    joined_at: Mapped[datetime] = mapped_column(DATETIME, server_default=text("CURRENT_TIMESTAMP"))

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), primary_key=True)
    course_id: Mapped[int] = mapped_column(ForeignKey("courses.id"), primary_key=True)

    user: Mapped["User"] = relationship(
        "User",
        back_populates="course_student"
    )
    course: Mapped["Course"] = relationship(
        "Course",
        back_populates="course_student"
    )

async def create_user(email: str, is_active: bool = True):
    async with async_session() as session:
        new_user = User(email=email, is_active=is_active)
        session.add(new_user)
        await session.commit()

async def get_user_by_id(user_id: int):
    async with async_session() as session:
        user = await session.get(User, user_id)
        return user

async def get_user_by_email(user_email: str):
    async with async_session() as session:
        stmt = select(User).where(User.email == user_email)
        user = await session.scalars(stmt)
        return user.first()

async def delete_user(user_id: int):
    async with async_session() as session:
        user = await session.get(User, user_id)
        if user:
            await session.delete(user)
            await session.commit()

async def create_course(title: str, description: str, author_id: int, is_published: bool = False):
    async with async_session() as session:
        new_course = Course(title=title, description=description, author_id=author_id, is_published=is_published)
        session.add(new_course)
        await session.commit()

async def get_course_by_id(course_id: int):
    async with async_session() as session:
        course = await session.get(Course, course_id)
        return course

async def get_courses_by_author(author_id: int):
    async with async_session() as session:
        stmt = select(Course).where(Course.author_id == author_id)
        courses = await session.scalars(stmt)
        return courses.all()

async def get_published_courses():
    async with async_session() as session:
        stmt = select(Course).where(Course.is_published.is_(True))
        courses = await session.scalars(stmt)
        return courses.all()

async def delete_course(course_id: int):
    async with async_session() as session:
        course = await session.get(Course, course_id)
        if course is None:
            return False

        await session.delete(course)
        await session.commit()
        return True

async def init_db():
    async with engine.begin() as conn:
        conn.run_sync(Base.metadata.create_all)

async def main():
    await init_db()

if __name__ == "__main__":
    asyncio.run(main())