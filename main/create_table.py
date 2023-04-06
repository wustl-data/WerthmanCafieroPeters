import psycopg2
from dotenv import load_dotenv
import os
import csv


import csv

def transform_csv(rows):
    # create a list of dictionaries with the desired format
    data = []
    for row in rows:
        row_dict = {}
        row_dict['Month'] = row[0]
        row_dict['Commodity'] = row[1]
        row_dict['Price'] = float(row[2])
        row_dict['(Unit, Currency)'] = row[3].strip('"').split(', ')
        row_dict['Symbol'] = row[4]
        data.append(row_dict)

    return data



import csv

def read_data(filename):
    """
    Reads data from a CSV file and returns it as a list of rows.
    """
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        rows = [row for row in reader]
        return rows[1:]  # skip the header row


# Completed functionality
def create_table(conn, table_name):
    """
    Creates a table with the specified name in the database connected to by conn.
    """
    with conn.cursor() as cur:
        cur.execute(
            f"CREATE TABLE IF NOT EXISTS {table_name} ("
            "id SERIAL PRIMARY KEY,"
            "Month DATE,"
            "Commodity TEXT,"
            "Price FLOAT,"
            "Currency TEXT,"
            "Symbol TEXT);"
        )
        conn.commit()

def drop_unit_column(conn):
    with conn.cursor() as cur:
        cur.execute(
            "ALTER TABLE commodities2 DROP COLUMN Unit;"
        )
        conn.commit()


def load_data(conn, table_name, filepath):
    """
    Loads data from a CSV file into the specified table in the database connected to by conn.
    """
    with open(filepath, 'r') as f:
        reader = csv.reader(f)
        next(reader) # skip header row
        for row in reader:
            print(row)
            with conn.cursor() as cur:
                cur.execute(
                    f"INSERT INTO {table_name} (Month, Commodity, Price, Currency, Symbol) VALUES (%s, %s, %s, %s, %s, %s);",
                    (row[0], row[1], float(row[2]), row[3], row[4], row[5])
                )
                conn.commit()




def table_exists(conn, table_name):
    """
    Checks if a table with the given name exists in the database connected to by conn.
    If the table exists, it prints information about the table.
    """
    with conn.cursor() as cur:
        cur.execute(
            f"SELECT EXISTS(SELECT relname FROM pg_class WHERE relname='{table_name}');"
        )
        table_exists = cur.fetchone()[0]
        if table_exists:
            print(f"Table {table_name} exists in the database.")
            cur.execute(f"SELECT * FROM {table_name};")
            rows = cur.fetchall()
            print(f"Table contains {len(rows)} rows.")
            for row in rows[:5]:
                print(row)
        else:
            print(f"Table {table_name} does not exist in the database.")



if __name__ == '__main__':
    load_dotenv()

    DB_HOST = os.getenv('DB_HOST')
    DB_PORT = os.getenv('DB_PORT')
    DB_NAME = os.getenv('DB_NAME')
    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')

    # Set up a connection to the database
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    #create_table(conn, 'commodities2')
    #table_exists(conn, 'commodities2')
    drop_unit_column(conn)
    #load_data(conn, 'commodities2', '/Users/michael/489856-489214-487404/melted_commodity_prices.csv')
    #table_name = "commodities"
    #if not table_exists(conn, 'commodities'):
       # create_table(conn, 'commodities')
   # else:
      #  print('table already exists')


    #data = read_data('/Users/michael/489856-489214-487404/melted_commodity_prices.csv')
    #transformed_data = transform_csv(data)

    #insert_data(conn, table_name, transformed_data)
    #create_table(conn, table_name)
   # insert_data(conn, table_name, data)







