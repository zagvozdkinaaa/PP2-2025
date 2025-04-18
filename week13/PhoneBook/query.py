import psycopg2
from config import load_config

def get_data():
    """ Retrieve data from the vendors table """
    config  = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT username, phone FROM phonebook WHERE phone LIKE %s", ('77%',))
                rows = cur.fetchall()
                print("Numbers that start with 77: ")
                for row in rows:
                    print(row)

                cur.execute("SELECT username, phone from phonebook WHERE username LIKE %s",('friend%',))
                rows =cur.fetchall()
                print("My friend's number: ")
                for row in rows:
                    print(row)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

if __name__ == '__main__':
    get_data()