from sqlalchemy import create_engine, Integer, String, ForeignKey, Numeric, Enum, DateTime, text
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship
from datetime import datetime

connection = "sqlite:///kino.db"
engine = create_engine(connection)

class Base(DeclarativeBase):
    pass

class Movie(Base):
    __tablename__ = "table_movies"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String)

    actors: Mapped[list["Actor"]] = relationship(
        "Actor",
        secondary="table_roles",
        back_populates="movies"
    )

    roles: Mapped[list["Role"]] = relationship(
        "Role",
        back_populates="movie"
    )

class Actor(Base):
    __tablename__ = "table_actors"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)

    movies: Mapped[list["Movie"]] = relationship(
        "Movie",
        secondary="table_roles",
        back_populates="actors"
    )

    roles: Mapped[list["Role"]] = relationship(
        "Role",
        back_populates="actor"
    )

class Role(Base):
    __tablename__ = "table_roles"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    salary: Mapped[float] = mapped_column(Numeric(10, 2))
    character_name: Mapped[str] = mapped_column(String)

    movie_id: Mapped[int] = mapped_column(ForeignKey("table_movies.id"))
    actor_id: Mapped[int] = mapped_column(ForeignKey("table_actors.id"))

    movie: Mapped["Movie"] = relationship(back_populates="roles")
    actor: Mapped["Actor"] = relationship(back_populates="roles")


Base.metadata.create_all(engine)