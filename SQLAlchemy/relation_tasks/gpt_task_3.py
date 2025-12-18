from sqlalchemy import (create_engine, Integer, String, CheckConstraint, Boolean,
                        DateTime, select, and_, desc, update, delete,
                        text)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from datetime import datetime

connection = "mysql+pymysql://root/root@localhost:3306/company"
engine = create_engine(connection)

class Base(DeclarativeBase):
    pass

class Employee(Base):
    __tablename__ = "employee_table"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    salary: Mapped[int] = mapped_column(Integer, default=50000)
    department: Mapped[str] = mapped_column(String, nullable=True)
    full_time: Mapped[bool] = mapped_column(Boolean, default=True)
    hired_at: Mapped[datetime] = mapped_column(DateTime, server_default=text("CURRENT_TIMESTAMP"))

Base.metadata.create_all(engine)


def add_employee(name, salary=None, department=None, full_time=True):
    with Session(engine) as session:
        new_employer = Employee(name=name, salary=salary, department=department, full_time=full_time)
        session.add(new_employer)
        session.commit()

add_employee("Vasya", None, None, True)

def get_employees_from_department(dep_name):
    with Session(engine) as session:
        stmt = select(Employee).where(Employee.department == dep_name)
        employees = session.scalars(stmt).all()
        for employer in employees:
            print(employer.name)

get_employees_from_department("Managers")

def get_senior_employees(min_salary):
    with Session(engine) as session:
        stmt = select(Employee).where(and_(Employee.salary >= min_salary, Employee.full_time == True)).order_by(desc(Employee.salary))
        employees = session.scalars(stmt).all()
        for employer in employees:
            print(employer.name, employer.salary)

get_senior_employees(4000)

def raise_salary_for_department(dep_name, percent):
    with Session(engine) as session:
        stmt = (
            update(Employee)
            .where(Employee.department == dep_name)
            .values(salary=Employee.salary * (1 + percent / 100))
        )

        session.execute(stmt)
        session.commit()

raise_salary_for_department("Backend", 15)


def delete_part_time_employees():
    with Session(engine) as session:
        stmt = delete(Employee).where(Employee.full_time == False)
        session.execute(stmt)
        session.commit()

delete_part_time_employees()