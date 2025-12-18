from sqlalchemy import create_engine, Integer, String, ForeignKey, Table
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship, Session
from sqlalchemy.ext.associationproxy import association_proxy

engine = create_engine("sqlite:///courses.db")

class Base(DeclarativeBase):
    pass

# таблица для many-to-many Student ↔ Course
enrollments = Table(
    "enrollments",
    Base.metadata,
    mapped_column("student_id", ForeignKey("students.id"), primary_key=True),
    mapped_column("course_id", ForeignKey("courses.id"), primary_key=True)
)

class Student(Base):
    __tablename__ = "students"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)

    courses_rel: Mapped[list["Course"]] = relationship("Course", secondary=enrollments, back_populates="students")
    courses: Mapped[list[str]] = association_proxy("courses_rel", "title")  # shortcut: названия курсов

class Instructor(Base):
    __tablename__ = "instructors"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)

    courses: Mapped[list["Course"]] = relationship("Course", back_populates="instructor")  # объекты Course

class Course(Base):
    __tablename__ = "courses"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String)

    instructor_id: Mapped[int] = mapped_column(ForeignKey("instructors.id"))
    instructor: Mapped["Instructor"] = relationship("Instructor", back_populates="courses")

    students: Mapped[list["Student"]] = relationship("Student", secondary=enrollments, back_populates="courses_rel")
    student_names: Mapped[list[str]] = association_proxy("students", "name")  # shortcut: имена студентов


def get_student_courses(student_id):
    with Session(engine) as session:
        student = session.get(Student, student_id)
        return student.courses

def get_course_students(course_id):
    with Session(engine) as session:
        course = session.get(Course, course_id)
        return course.student_names

def get_instructor_students(instructor_id):
    with Session(engine) as session:
        instructor = session.get(Instructor, instructor_id)
        return [student.name for course in instructor.courses for student in course.students]

def get_course_instructor(course_id):
    with Session(engine) as session:
        course = session.get(Course, course_id)
        return course.instructor.name

Base.metadata.create_all(engine)