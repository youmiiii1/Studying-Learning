from sqlalchemy import create_engine, Integer, String, ForeignKey, DateTime, text, Numeric, Text, Enum, select
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship, Session
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

    assignment: Mapped[list["Assignment"]] = relationship(
        "Assignment",
        back_populates="user"
    )

    projects = association_proxy("assignment", "project")
    roles_in_projects = association_proxy("assignment", "role")

class Project(Base):
    __tablename__ = "table_project"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(Text)

    assignment: Mapped[list["Assignment"]] = relationship(
        "Assignment",
        back_populates="project"
    )

    users = association_proxy("assignment", "user")
    roles = association_proxy("assignment", "role")

class Role(Base):
    __tablename__ = "table_role"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(Enum("admin", "developer", "reviewer"), name="role_name")

    assignment: Mapped[list["Assignment"]] = relationship(
        "Assignment",
        back_populates="role"
    )

class Assignment(Base):
    __tablename__ = "table_assignment"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    assigned_at: Mapped[datetime] = mapped_column(DateTime, server_default=text("CURRENT_TIMESTAMP"))

    user_id: Mapped[int] = mapped_column(ForeignKey("table_user.id"))
    project_id: Mapped[int] = mapped_column(ForeignKey("table_project.id"))
    role_id: Mapped[int] = mapped_column(ForeignKey("table_role.id"))

    user: Mapped["User"] = relationship(
        "User",
        back_populates="assignment"
    )

    project: Mapped["Project"] = relationship(
        "Project",
        back_populates="assignment"
    )

    role: Mapped["Role"] = relationship(
        "Role",
        back_populates="assignment"
    )

def get_user_projects(user_id):
    with Session(engine) as session:
        user = session.get(User, user_id)
        return user.projects

def get_project_users(project_id):
    with Session(engine) as session:
        project = session.get(Project, project_id)
        return project.users

def get_user_roles(user_id):
    with Session(engine) as session:
        user = session.get(User, user_id)
        return user.roles_in_projects

def get_user_project_roles(user_id):
    with Session(engine) as session:
        user = session.get(User, user_id)
        return[(a.project.title, a.role.name) for a in user.assignment]

def get_users_with_role_in_project(project_id, role_name):
    with Session(engine) as session:
        project = session.get(Project, project_id)
        return [
            a.user
            for a in project.assignment
            if a.role.name == role_name
        ]


Base.metadata.create_all(engine)