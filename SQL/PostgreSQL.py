import psycopg2
from Config_PostgreSQL_db import host, db_name, db_user, db_password, port

# ---- Пример импорта extensions для настройки уровней безопасности ---- #
from psycopg2 import extensions

db = None

# ---- Пример подключения к таблице ---- #
try:
    db = psycopg2.connect(
        host = host,
        database = db_name,
        user = db_user,
        password = db_password,
        port = port
    )

    # ---- Пример создания autocommit ---- #
    db.autocommit = True

    # ---- Пример настройки уровней изоляции транзакций ---- #
    # ---- Read Committed - 1 ---- #
    read_committed = extensions.ISOLATION_LEVEL_READ_COMMITTED
    db.set_isolation_level(read_committed)

    # ---- Repeatable Read - 2 ---- #
    repeatable_read = extensions.ISOLATION_LEVEL_REPEATABLE_READ
    db.set_isolation_level(repeatable_read)

    # ---- Serializable - 3 ---- #
    serializable = extensions.ISOLATION_LEVEL_SERIALIZABLE
    db.set_isolation_level(serializable)

    # ---- Read Uncommitted - 4 ---- #
    read_uncommitted = extensions.ISOLATION_LEVEL_READ_UNCOMMITTED
    db.set_isolation_level(read_uncommitted)

    # ---- Узнаем какой текущий уровень изоляции 'В цифре' ---- #
    current_iso_level = db.isolation_level
    print(f"Current isolation level is: {current_iso_level}")

    # ---- Пример создания курсора ---- #
    with db.cursor() as cur:

        # ---- Пример cur.execute создания таблицы ---- #
        cur.execute("""
                    CREATE TABLE people(
                        id BIGSERIAL PRIMARY KEY,
                        name VARCHAR(256) NOT NULL,
                        age INT NOT NULL,
                        email VARCHAR(30) UNIQUE NOT NULL
                    );""")

        # ---- Пример cur.execute добавления данных в таблицу ---- #
        cur.execute("""
                    INSERT INTO people (name, age, email) VALUES
                        ('Michael', 22, 'miha@gmail.com'),
                        ('Seva', 17, 'seva@gmail.com'),
                        ('Babushka', 64, 'sveta@gmail.com'),
                        ('Mama', 44, 'anna@gmail.com')
                """)

        # ---- Пример cur.executemany ---- #
        sql_query = 'INSERT INTO people(name, age, email) VALUES(%s, %s, %s)'
        data_table = [
            ('Ogla', 21, 'olga@gmail.com'),
            ('Danil', 23, 'danil@gmail.com'),
            ('Keria', 23, 'keria@gmail.com'),
        ]
        cur.executemany(sql_query, data_table)

        # ---- Пример получения текущего уровня безопасности транзакции 'Через SQL' ---- #
        cur.execute("SHOW transaction_isolation;")
        print(cur.fetchone())

        # ---- Пример fetchone ---- #
        cur.execute("SELECT * FROM people")
        print(cur.fetchone())

        # ---- Пример fetchall ---- #
        cur.execute("SELECT * FROM people")
        print(cur.fetchall())

        # ---- Пример fetchmany ---- #
        cur.execute("SELECT * FROM people")
        print(cur.fetchmany(3))

        # ---- Пример создание функции search_user_by_id ---- #
        cur.execute("""
                    CREATE OR REPLACE FUNCTION search_user_by_id(p_id int4)
                    RETURNS text AS $$
                    BEGIN
                      RETURN (SELECT last_name||' '||first_name||' '||middle_name FROM list_users WHERE id = p_id);
                    END;
                    $$ LANGUAGE plpgsql;
                """)

        # ---- Пример вызова функции search_user_by_id через cur.callproc ---- #
        cur.callproc('search_user_by_id', [5])

        # ---- Получаем результат работы функции из курсора ---- #
        res = cur.fetchone()
        print(f"Информация о пользователе: {res[0]}")

    db.commit()

except Exception as e:
    # ---- Пример отката запроса ---- #
    db.rollback()

    print(f"Error: {e}")

# ---- Пример закрытия запроса ---- #
finally:
    if db:
        db.close()