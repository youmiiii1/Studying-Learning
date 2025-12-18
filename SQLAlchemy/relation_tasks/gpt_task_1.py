from sqlalchemy import Integer, String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column


connection = "sqlite:///test.db"
engine =create_engine(connection)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "test_table"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String, unique=True)
    age: Mapped[int] = mapped_column(Integer)

Base.metadata.create_all(engine)

def add_user(user_name, user_age):
    with Session(engine) as session:
        new_user = User(username=user_name, age=user_age)
        session.add(new_user)
        session.commit()

add_user("Michael", 22)

def show_all_users(age_filter):
    with Session(engine) as session:
        stmt = select(User).where(User.age > age_filter)
        all_users = session.scalars(stmt).all()
        return all_users

show_all_users(20)