from sqlalchemy import create_engine, Integer, String, ForeignKey
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship

connection = "sqlite:///company.db"
engine = create_engine(connection)

class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String)

    assignments: Mapped[list["Assignment"]] = relationship(
        "Assignment",
        back_populates="user"
    )

    projects_proxy = association_proxy("assignments", "project")
    roles_proxy = association_proxy("assignments", "role")


class Project(Base):
    __tablename__ = "project_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String)

    assignments: Mapped[list["Assignment"]] = relationship(
        "Assignment",
        back_populates="project"
    )

    users_proxy = association_proxy("assignments", "user")


class Role(Base):
    __tablename__ = "role_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)

    assignments: Mapped[list["Assignment"]] = relationship(
        "Assignment",
        back_populates="role"
    )


class Assignment(Base):
    __tablename__ = "assignment_table"

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("user_table.id"))
    project_id: Mapped[int] = mapped_column(ForeignKey("project_table.id"))
    role_id: Mapped[int] = mapped_column(ForeignKey("role_table.id"))

    user: Mapped["User"] = relationship(
        "User",
        back_populates="assignments"
    )

    project: Mapped["Project"] = relationship(
        "Project",
        back_populates="assignments"
    )

    role: Mapped["Role"] = relationship(
        "Role",
        back_populates="assignments"
    )


Base.metadata.create_all(engine)


def get_user_projects(session, user_id):
    user = session.get(User, user_id)
    return user.projects_proxy

def get_project_users(session, project_id):
    project = session.get(Project, project_id)
    return project.users_proxy

def get_user_roles(session, user_id):
    user = session.get(User, user_id)
    return user.roles_proxy

def get_user_project_roles(session, user_id):
    user = session.get(User, user_id)
    return [
        (a.project.tile, a.role.name)
            for a in user.assigment
        ]

def get_users_with_role_in_project(session, project_id, role_name):
    project = session.get(Project, project_id)
    return [
        user.username
        for user in project.assignments.user
        if any(role == role_name for role in project.assignments.role)
        ]

