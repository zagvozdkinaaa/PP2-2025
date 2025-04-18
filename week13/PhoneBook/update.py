import psycopg2
from config import load_config

def update_user_data():
    """ Update user's username or phone number based on user input """
    
    try:
        # Ask for the user ID whose data you want to update
        user_id = int(input("Enter the user ID to update: "))

        # Ask for the new username, if provided
        new_username = input("Enter new username (leave blank to keep unchanged): ")
        if not new_username:
            new_username = None  # If empty, keep the old value

        # Ask for the new phone number, if provided
        new_phone = input("Enter new phone (leave blank to keep unchanged): ")
        if not new_phone:
            new_phone = None  # If empty, keep the old value

        # Prepare the SQL query for updating data
        sql = """UPDATE phonebook
                 SET username = %s, phone = %s
                 WHERE id = %s"""

        # Modify the SQL query if only one field is provided
        if new_username is None:
            sql = """UPDATE phonebook
                     SET phone = %s
                     WHERE id = %s"""
        elif new_phone is None:
            sql = """UPDATE phonebook
                     SET username = %s
                     WHERE id = %s"""

        # Database connection configuration
        config = load_config()

        updated_row_count = 0

        try:
            with psycopg2.connect(**config) as conn:
                with conn.cursor() as cur:
                    # Execute the update query based on provided fields
                    if new_username is not None and new_phone is not None:
                        cur.execute(sql, (new_username, new_phone, user_id))
                    elif new_username is not None:
                        cur.execute(sql, (new_username, user_id))
                    elif new_phone is not None:
                        cur.execute(sql, (new_phone, user_id))

                    # Get the count of updated rows
                    updated_row_count = cur.rowcount

                # Commit the changes to the database
                conn.commit()

        except (Exception, psycopg2.DatabaseError) as error:
            print(f"Error: {error}")

        # Output the result of the update
        if updated_row_count > 0:
            print(f"Updated {updated_row_count} row(s).")
        else:
            print("No rows were updated.")
    
    except ValueError:
        # Handle invalid input for user ID
        print("Invalid input. Please enter a valid user ID.")

if __name__ == '__main__':
    update_user_data()

