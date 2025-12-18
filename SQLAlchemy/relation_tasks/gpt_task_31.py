from sqlalchemy import create_engine, Integer, String, ForeignKey, Table
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.ext.associationproxy import association_proxy

engine = create_engine("sqlite:///tracker.db")


class Base(DeclarativeBase):
    pass


# many-to-many Ticket ↔ Label
ticket_labels = Table(
    "ticket_labels",
    Base.metadata,
    mapped_column("ticket_id", ForeignKey("tickets.id"), primary_key=True),
    mapped_column("label_id", ForeignKey("labels.id"), primary_key=True)
)


class Developer(Base):
    __tablename__ = "developers"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)

    assignments: Mapped[list["Assignment"]] = relationship(
        "Assignment",
        back_populates="developer"
    )

    tickets_proxy = association_proxy("assignments", "ticket")
    roles_proxy = association_proxy("assignments", "role")


class Ticket(Base):
    __tablename__ = "tickets"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String)

    assignments: Mapped[list["Assignment"]] = relationship(
        "Assignment",
        back_populates="ticket"
    )

    developers_proxy = association_proxy("assignments", "developer")

    labels_rel: Mapped[list["Label"]] = relationship(
        "Label",
        secondary=ticket_labels,
        back_populates="tickets"
    )

    labels_proxy = association_proxy("labels_rel", "name")


class Label(Base):
    __tablename__ = "labels"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)

    tickets: Mapped[list["Ticket"]] = relationship(
        "Ticket",
        secondary=ticket_labels,
        back_populates="labels_rel"
    )


class Assignment(Base):
    __tablename__ = "assignments"

    id: Mapped[int] = mapped_column(primary_key=True)

    developer_id: Mapped[int] = mapped_column(ForeignKey("developers.id"))
    ticket_id: Mapped[int] = mapped_column(ForeignKey("tickets.id"))
    role: Mapped[str] = mapped_column(String)   # "assignee", "reviewer", etc.

    developer: Mapped["Developer"] = relationship(
        "Developer",
        back_populates="assignments"
    )
    ticket: Mapped["Ticket"] = relationship(
        "Ticket",
        back_populates="assignments"
    )


Base.metadata.create_all(engine)

def get_developer_tickets(session, dev_id):
    developer = session.get(Developer, dev_id)
    return developer.tickets_proxy

def get_ticket_developers(session, ticket_id):
    ticket = session.get(Ticket, ticket_id)
    return ticket.developers_proxy

def get_developer_roles(session, dev_id):
    developer = session.get(Developer, dev_id)
    return developer.roles_proxy

def get_developer_ticket_roles(session, dev_id):
    developer = session.get(Developer, dev_id)
    return [
        (a.ticket.title, a.role)
        for a in developer.assignments
    ]

def get_devs_by_role_in_ticket(session, ticket_id, role_name):
    ticket = session.get(Ticket, ticket_id)
    return [
        a.developer.name
        for a in ticket.assignments
        if a.role == role_name
    ]