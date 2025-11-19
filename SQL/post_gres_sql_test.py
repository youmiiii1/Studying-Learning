import psycopg2
from Config_PostgreSQL_db import host, db_name, db_user, db_password, port

db = None

try:
    db = psycopg2.connect(
        host = host,
        database = db_name,
        user = db_user,
        password = db_password,
        port = port
    )

    with db.cursor() as cur:
        cur.execute("SELECT * FROM people")

        print(cur.fetchmany(2))

except Exception as e:
    db.rollback()

finally:
    if db:
        db.close()