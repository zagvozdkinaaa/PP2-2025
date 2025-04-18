import psycopg2
from config import load_config

def upload_data_from_csv(csv_file_path):
    """ Upload data from a CSV file into the PostgreSQL table """
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # Загружаем данные из CSV в таблицу phonebook
                with open(csv_file_path, 'r') as f:
                    # Пропускаем заголовок CSV
                    next(f)
                    # Используем команду COPY для загрузки данных
                    cur.copy_from(f, 'phonebook', sep=',', columns=('username', 'phone'))
                conn.commit()
                print(f"Data from {csv_file_path} uploaded successfully.")
    except (psycopg2.DatabaseError, Exception) as error:
        print(f"Error: {error}")

if __name__ == '__main__':
    upload_data_from_csv('/Users/zagvozdkinaaa/PP2/week13/PhoneBook/phonebook_data.csv')
