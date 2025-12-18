from sqlalchemy import create_engine, Integer, String, ForeignKey, DateTime, text
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship
from datetime import datetime

connection = "sqlite:///kino.db"
engine = create_engine(connection)

class Base(DeclarativeBase):
    pass


# ---------------- USER ----------------
class User(Base):
    __tablename__ = "table_users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String)

    devices: Mapped[list["Device"]] = relationship(
        "Device",
        back_populates="user"
    )

    enrollments: Mapped[list["WatchHistory"]] = relationship(
        "WatchHistory",
        back_populates="user"
    )


# ---------------- MOVIE ----------------
class Movie(Base):
    __tablename__ = "table_movies"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String)
    year: Mapped[int] = mapped_column(Integer)

    enrollments: Mapped[list["WatchHistory"]] = relationship(
        "WatchHistory",
        back_populates="movie"
    )


# ---------------- DEVICE ----------------
class Device(Base):
    __tablename__ = "table_devices"

    id: Mapped[int] = mapped_column(primary_key=True)
    device_name: Mapped[str] = mapped_column(String)

    user_id: Mapped[int] = mapped_column(ForeignKey("table_users.id"))

    user: Mapped["User"] = relationship(
        "User",
        back_populates="devices"
    )

    enrollments: Mapped[list["WatchHistory"]] = relationship(
        "WatchHistory",
        back_populates="device"
    )


# ---------------- HISTORY ----------------
class WatchHistory(Base):
    __tablename__ = "enrollments"

    id: Mapped[int] = mapped_column(primary_key=True)
    watched_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=text("CURRENT_TIMESTAMP")
    )
    duration_seconds: Mapped[int] = mapped_column(Integer)

    user_id: Mapped[int] = mapped_column(ForeignKey("table_users.id"))
    movie_id: Mapped[int] = mapped_column(ForeignKey("table_movies.id"))
    device_id: Mapped[int] = mapped_column(ForeignKey("table_devices.id"))

    user: Mapped["User"] = relationship(
        "User",
        back_populates="enrollments"
    )

    movie: Mapped["Movie"] = relationship(
        "Movie",
        back_populates="enrollments"
    )

    device: Mapped["Device"] = relationship(
        "Device",
        back_populates="enrollments"
    )


Base.metadata.create_all(engine)