from sqlalchemy import create_engine, ForeignKey, Integer, String, Text, DateTime
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship
from datetime import datetime

connection = "sqlite:///social_media.db"
engine = create_engine(connection)

class Base(DeclarativeBase):
    pass

class Student(Base):
    __tablename__ = "table_students"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)

    courses: Mapped[list["Course"]] = relationship(
        "Course",
        back_populates="students",
        secondary="table_enrollment"
    )

class Course(Base):
    __tablename__ = "table_courses"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String)

    students: Mapped[list["Student"]] = relationship(
        "Student",
        back_populates="courses",
        secondary="table_enrollment"
    )

class Enrollment(Base):
    __tablename__ = "table_enrollment"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    progress: Mapped[int] = mapped_column(Integer)
    started_at: Mapped[datetime] = mapped_column(DateTime, server_default="CURRENT_TIMESTAMP")
    student_id: Mapped[int] = mapped_column(ForeignKey("table_students.id"))
    course_id: Mapped[int] = mapped_column(ForeignKey("table_courses.id"))

Base.metadata.create_all(engine)