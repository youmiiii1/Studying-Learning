from sqlalchemy import create_engine, Integer, String, Text, ForeignKey, DateTime, text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.ext.associationproxy import association_proxy
from datetime import datetime

#PostgreSQL
connection = "postgresql+psycopg2://postgres:postgres@localhost:5432/academy_db"

#MySQL
connection_2 = "mysql+pymysql://root:root@localhost:3306/academy_db"

#SQLite
connection_3 = "sqlite:///academy.db"

engine = create_engine(connection)

class Base(DeclarativeBase):
    pass

class Course(Base):
    __tablename__ = "courses"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(150), nullable=False)
    description: Mapped[str] = mapped_column(Text)

    enrollments: Mapped[list["Enrollment"]] = relationship(back_populates="course")
    students = association_proxy("enrollments", "student")

class Student(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False, unique=True)

    enrollments: Mapped[list["Enrollment"]] = relationship(back_populates="student")
    courses = association_proxy("enrollments", "course")

class Enrollment(Base):
    __tablename__ = "enrollments"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    student_id: Mapped[int] = mapped_column(ForeignKey("students.id"))
    course_id: Mapped[int] = mapped_column(ForeignKey("courses.id"))

    student: Mapped["Student"] = relationship(back_populates="enrollments")
    course: Mapped["Course"] = relationship(back_populates="enrollments")

class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    content: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=text("CURRENT_TIMESTAMP"))

    post_tags: Mapped[list["PostTag"]] = relationship(back_populates="post")
    tags = association_proxy("post_tags", "tag")

class Tag(Base):
    __tablename__ = "tags"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(80), nullable=False, unique=True)

    post_tags: Mapped[list["PostTag"]] = relationship(back_populates="tag")
    posts = association_proxy("post_tags", "post")

class PostTag(Base):
    __tablename__ = "post_tags"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id", ondelete="CASCADE"))
    tag_id: Mapped[int] = mapped_column(ForeignKey("tags.id", ondelete="CASCADE"))

    post: Mapped["Post"] = relationship(back_populates="post_tags")
    tag: Mapped["Tag"] = relationship(back_populates="post_tags")

Base.metadata.create_all(engine)

