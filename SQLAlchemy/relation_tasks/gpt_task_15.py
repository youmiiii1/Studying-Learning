from sqlalchemy import create_engine, Integer, String, ForeignKey, Numeric, Enum, DateTime, text
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship
from datetime import datetime

connection = "sqlite:///kino.db"
engine = create_engine(connection)


class Base(DeclarativeBase):
    pass

class Course(Base):
    __tablename__ = "table_courses"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String)

class Student(Base):
    __tablename__ = "table_students"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)

    progress: Mapped[list["Progress"]] = relationship(
        "Progress",
        back_populates="student"
    )

class Module(Base):
    __tablename__ = "table_module"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String)
    course_id: Mapped[int] = mapped_column(ForeignKey("table_courses.id"))

    progress: Mapped[list["Progress"]] = relationship(
        "Progress",
        back_populates="module"
    )

class Progress(Base):
    __tablename__ = "table_progress"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    status: Mapped[str] = mapped_column(Enum("not_started", "in_progress", "completed", name="progress_status"))
    score: Mapped[int] = mapped_column(Integer, nullable=True)
    updated_at: Mapped[datetime] = mapped_column(DateTime, server_default=text("CURRENT_TIMESTAMP"))

    student_id: Mapped[int] = mapped_column(ForeignKey("table_students.id"))
    module_id: Mapped[int] = mapped_column(ForeignKey("table_module.id"))

    student: Mapped["Student"] = relationship(back_populates="progress")
    module: Mapped["Module"] = relationship(back_populates="progress")

Base.metadata.create_all(engine)