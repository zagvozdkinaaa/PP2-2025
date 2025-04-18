import psycopg2
from config import load_config


def delete_contact():
    """ Delete part by part id """
    username=input("Enter username to delete: ")
    phone=input("Enter phone to delete: ")

    rows_deleted  = 0
    config = load_config()

    if not username and not phone:
        print("Please enter username or phone to delete.")
        return rows_deleted
    if username and phone:
        sql = 'DELETE FROM phonebook WHERE username = %s OR phone = %s'
        params=(username, phone)
    elif username:
        sql = 'DELETE FROM phonebook WHERE username = %s'
        params = (username,)
    else:
        sql = 'DELETE FROM phonebook WHERE phone = %s'
        params=(phone,)

    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the UPDATE statement
                cur.execute(sql, params)
                rows_deleted = cur.rowcount

            # commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return rows_deleted

if __name__ == '__main__':
    deleted_rows = delete_contact()
    print('The number of deleted rows: ', deleted_rows)