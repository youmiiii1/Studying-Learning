# Example - 1
class User:
    def __init__(self, email):
        self.__class__.validate(email)
        self.email = email

    @classmethod
    def validate(cls, email):
        if email.count("@") != 1:
            raise ValueError("You can use only one '@'")

        name, domain = email.split("@")

        if not name:
            raise ValueError("Email must have name before '@'")

        if "." not in domain:
            raise ValueError("Domain must have '.'")

        if domain.startswith(".") or domain.endswith("."):
            raise ValueError("You can't use '.' as first/last sign.")

        if not domain[0].isalpha() or not domain[-1].isalpha():
            raise ValueError("You must use only letters as your first/last signs.")

        if " " in email:
            raise ValueError("You must not use space in your email")

        for ch in email:
            if ch.isupper():
                raise ValueError("You can't use upper case letters in your email.")

User.validate("hillo1@oog1le.com")

# Example - 2
import random

class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id_ = id_
        self.name = name
        self.company = company
        self._workers = []

    def add_worker(self, worker):
        if worker not in self._workers:
            self._workers.append(worker)

    @property
    def workers(self):
        return self._workers

class Worker:
    def __init__(self, id_: int, name: str, company: str, boss):
        self.id_ = id_
        self.name = name
        self.company = company
        self._boss = None
        self.boss = boss

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, value):
        if not isinstance(value, Boss):
            raise ValueError("boss must be an instance of Boss")

        self._boss = value
        value.add_worker(self)

boss1 = Boss(1, "Bob", "Admitors")
worker1 = Worker(101, "Alice", "Admitors", boss1)

print([w.name for w in boss1.workers])
print(worker1.boss.name)

# Example - 3
from functools import wraps

class TypeDecorators:
    @staticmethod
    def to_int(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return int(result)
        return wrapper

    @staticmethod
    def to_str(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return str(result)
        return wrapper

    @staticmethod
    def to_float(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return float(result)
        return wrapper

    @staticmethod
    def to_bool(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return bool(result)
        return wrapper