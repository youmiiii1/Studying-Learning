from sqlalchemy import create_engine, Integer, String, ForeignKey
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship

connection = "postgresql+psycopg2://postgres:posgres@localhost:5432/academy_db"

engine = create_engine(connection)

class Base(DeclarativeBase):
    pass


class Student(Base):
    __tablename__ = "table_students"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String)

    # many-to-many через Enrollment
    enrollments: Mapped[list["Enrollment"]] = relationship(back_populates="student")

    # association_proxy
    courses = association_proxy("enrollments", "course")
    teachers = association_proxy("courses", "teacher")  # ВАЖНО: идём через courses!


class Course(Base):
    __tablename__ = "table_courses"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)

    # many-to-many через Enrollment
    enrollments: Mapped[list["Enrollment"]] = relationship(back_populates="course")

    # связь "много курсов — один учитель"
    teacher_id: Mapped[int] = mapped_column(ForeignKey("table_teachers.id"))
    teacher: Mapped["Teacher"] = relationship(back_populates="courses")

    students = association_proxy("enrollments", "student")


class Teacher(Base):
    __tablename__ = "table_teachers"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)

    # один учитель — много курсов
    courses: Mapped[list["Course"]] = relationship(back_populates="teacher")

    # через courses → enrollments → students
    students = association_proxy("courses", "students")


class Enrollment(Base):
    __tablename__ = "enrollments"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    student_id: Mapped[int] = mapped_column(ForeignKey("table_students.id"))
    course_id: Mapped[int] = mapped_column(ForeignKey("table_courses.id"))

    student: Mapped["Student"] = relationship(back_populates="enrollments")
    course: Mapped["Course"] = relationship(back_populates="enrollments")



