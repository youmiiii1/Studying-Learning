import sqlite3

db = sqlite3.connect('test_database.db')

# ---- Пример изменения формата возврата строк после метода SELECT (Заметка - 1.1)---- #
db.row_factory = sqlite3.Row

cur = db.cursor()

users = [
    ('Michael', "Nahornyi", '+380'),
    ('Olga', "Pokoliukina", '+7'),
    ('Seva', "Nahornyi", '+445'),
    ('Hanna', "Ryzhakova", '+4412'),
]

# ---- Пример создания таблицы ---- #
cur.execute("""CREATE TABLE users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
first_name TEXT NOT NULL,
last_name TEXT NOT NULL,
phone TEXT UNIQUE NOT NULL
)""")

# ---- Пример - 1. Добавления данных в таблицу ---- #
for user in users:
    cur.execute("INSERT INTO users (first_name, last_name, phone) VALUES(?, ?, ?)", user)

# ---- Пример - 2. Добавления данных в таблицу ---- #
cur.executemany("INSERT INTO users (first_name, last_name, phone) VALUES(?, ?, ?)", users)

# ---- Пример добавления нескольких SQL запросов одной командой ---- #
sql = """CREATE TABLE cars(
id INTEGER PRIMARY KEY AUTOINCREMENT,
mark TEXT NOT NULL
);

INSERT INTO cars(mark) VALUES('Audi');
INSERT INTO cars(mark) VALUES('BMW');
"""

cur.executescript(sql)

# ---- LAST_INSERT_ID() = cur.lastrowid ---- #
cur.execute("INSERT INTO ***(***, ***) VALUES(?, ?)", ('***', '***'))
last_id = cur.lastrowid

cur.execute("INSERT INTO ***(***, ***) VALUES(?, ?)", ('***', last_id))

# ---- Пример db.rollback() ---- #
try:
    cur.execute("""CREATE TABLE ***(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
    );""")

    cur.executemany("INSERT INTO ***(***, ***) VALUES(?, ?)", users)

    cur.execute("UPDATE *** SET *** = 0 WHERE *** = '***' OR *** = '***'")

    raise ValueError

except sqlite3.Error as e:
    print("Произошла ошибка:", {e})
    db.rollback()

finally:
    db.close()

# ---- Пример cur.fetchmany ---- #
cur.execute("SELECT * FROM people")
temp = cur.fetchmany(2)
print(temp)

# ---- Пример cur.fetchone ---- #
cur.execute("SELECT * FROM people")
temp = cur.fetchone()
print(temp)

# ---- Пример cur.fetchall ---- #
cur.execute("SELECT * FROM people")
temp = cur.fetchall()
print(temp)

# ---- Пример возврата значений SELECT через словарь (Заметка - 1.1)---- #
cur.execute("SELECT * FROM people")
for el in cur:
    print(el['name'], el['age'])

# ---- Пример добавления фото / BLOB в таблицу ---- #
def insert_photo(n):
    try:
        with open(F"{n}.png", "rb") as photo:
            return photo.read()

    except IOError as e:
        print(e)
        raise False

img = insert_photo('Mongol')
binary = sqlite3.Binary(img)
cur.execute("INSERT INTO people(name, ava) VALUES(?, ?)", ('Seva', binary))

# ---- Пример выкачки фото из таблицы / BLOB на ПК ---- #
def download_photo(name, data):
    try:
        with open(name, 'wb') as photo:
            photo.write(data)

    except IOError as e:
        print(e)
        return False

cur.execute("SELECT ava FROM people WHERE name = 'Mangol'")
img = cur.fetchone()['ava']
download_photo('out.png', img)

# ---- Пример копирования базы данных через iterdump ---- #
def copy_database():
    with open('copy_base.txt', 'w') as copied_file:
        for sql in db.iterdump():
            copied_file.write(sql)

copy_database()

# ---- Пример воссоздания базы данных через iterdump ---- #
def re_build_base():
    with open('copy_base.txt', 'r') as f:
        sql = f.read()
        cur.executescript(sql)

re_build_base()

# ---- Пример использования конструкции CASE ---- #
cur.execute("""SELECT name, size,
CASE
WHEN size >= 70 AND population >= 5 THEN 'Большая'
WHEN size <= 40 AND population <= 5 THEN 'Маленькая'
ELSE 'Средняя'
END AS named_size
FROM planets;
""")

db.commit()
db.close()