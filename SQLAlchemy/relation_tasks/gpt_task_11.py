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
    class_name: Mapped[str] = mapped_column(String)

    grades: Mapped[list["Grades"]] = relationship(back_populates="student")

class Subject(Base):
    __tablename__ = "table_subjects"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String)

    grades: Mapped[list["Grades"]] = relationship(back_populates="subject")
    teacher: Mapped["Teachers"] = relationship(back_populates="subject")

class Grades(Base):
    __tablename__ = "table_grades"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    grade_value: Mapped[int] = mapped_column(Integer)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default="CURRENT_TIMESTAMP")
    student_id: Mapped[int] = mapped_column(ForeignKey("table_students.id"))
    subject_id: Mapped[int] = mapped_column(ForeignKey("table_subjects.id"))

    student: Mapped["Student"] = relationship(back_populates="grades")
    subject: Mapped["Subject"] = relationship(back_populates="grades")

class Teachers(Base):
    __tablename__ = "table_teachers"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    subject_id: Mapped[int] = mapped_column(ForeignKey("table_subjects.id"))

    subject: Mapped["Subject"] = relationship(back_populates="teacher")

Base.metadata.create_all(engine)