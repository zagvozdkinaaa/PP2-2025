import psycopg2
from config import load_config

def create_table():
    """ Create tables in the PostgreSQL database"""
    command = (
        """
        CREATE TABLE phonebook (
            id SERIAL PRIMARY KEY,
            username VARCHAR(255) NOT NULL,
            phone VARCHAR(255) NOT NULL
        )
        """)
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # execute the CREATE TABLE statement
                cur.execute(command)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    create_table()