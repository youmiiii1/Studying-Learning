from sqlalchemy import create_engine, Integer, String, ForeignKey, DateTime, text, Numeric, Text
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship
from datetime import datetime

connection = "sqlite:///kino.db"
engine = create_engine(connection)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "table_user"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String)

    enrollment: Mapped[list["Enrollment"]] = relationship(
        "Enrollment",
        back_populates="user"
    )

    reviews: Mapped[list["Review"]] = relationship(
        "Review",
        back_populates="user"
    )


class Course(Base):
    __tablename__ = "table_course"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(Text)

    enrollment: Mapped[list["Enrollment"]] = relationship(
        "Enrollment",
        back_populates="course"
    )

    lessons: Mapped[list["Lesson"]] = relationship(
        "Lesson",
        back_populates="course"
    )

    reviews: Mapped[list["Review"]] = relationship(
        "Review",
        back_populates="course"
    )

class Lesson(Base):
    __tablename__ = "table_lesson"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String)
    video_url: Mapped[str] = mapped_column(Text)

    course_id: Mapped[int] = mapped_column(ForeignKey("table_course.id"))

    course: Mapped["Course"] = relationship(
        "Course",
        back_populates="lessons"
    )

class Review(Base):
    __tablename__ = "table_review"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    review_text: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=text("CURRENT_TIMESTAMP"))

    course_id: Mapped[int] = mapped_column(ForeignKey("table_course.id"))

    course: Mapped["Course"] = relationship(
        "Course",
        back_populates="reviews"
    )

    user_id: Mapped[int] = mapped_column(ForeignKey("table_user.id"))

    user: Mapped["User"] = relationship(
        "User",
        back_populates="reviews"
    )

class Enrollment(Base):
    __tablename__ = "table_enrollment"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    enrolled_at: Mapped[datetime] = mapped_column(DateTime, server_default=text("CURRENT_TIMESTAMP"))

    user_id: Mapped[int] = mapped_column(ForeignKey("table_user.id"))
    course_id: Mapped[int] = mapped_column(ForeignKey("table_course.id"))

    user: Mapped["User"] = relationship(
        "User",
        back_populates="enrollment"
    )

    course: Mapped["Course"] = relationship(
        "Course",
        back_populates="enrollment"
    )


Base.metadata.create_all(engine)
