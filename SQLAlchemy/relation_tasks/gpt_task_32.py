from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, DeclarativeBase


class Base(DeclarativeBase):
    pass


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # many-to-many через ассоциацию
    assignments = relationship("StudentCourseAssignment", back_populates="student")

    # proxy: список курсов
    courses_proxy = relationship(
        "Course",
        secondary="student_course_assignments",
        viewonly=True
    )

    # proxy: список ролей студента на всех курсах
    roles_proxy = relationship(
        "StudentCourseAssignment",
        viewonly=True
    )


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)

    assignments = relationship("StudentCourseAssignment", back_populates="course")

    # proxy: список студентов
    students_proxy = relationship(
        "Student",
        secondary="student_course_assignments",
        viewonly=True
    )


class StudentCourseAssignment(Base):
    __tablename__ = "student_course_assignments"

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    course_id = Column(Integer, ForeignKey("courses.id"))
    role = Column(String, nullable=False)

    student = relationship("Student", back_populates="assignments")
    course = relationship("Course", back_populates="assignments")

def get_student_courses(session, student_id):
    student = session.get(Student, student_id)
    return student.courses_proxy

def get_course_students(session, course_id):
    course = session.get(Course, course_id)
    return course.students_proxy

def get_student_roles(session, student_id):
    student = session.get(Student, student_id)
    return student.roles_proxy

def get_student_course_roles(session, student_id):
    student = session.get(Student, student_id)
    return [
        (a.course.title, a.role)
        for a in student.assignments
    ]

def get_students_with_role_in_course(session, course_id, role_name):
    course = session.get(Course, course_id)
    return [a.student.name for a in course.assignments if a.role.name == role_name]