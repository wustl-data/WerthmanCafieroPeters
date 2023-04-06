import psycopg2
from dotenv import load_dotenv
import os

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

# Open a cursor to perform database operations
cur = conn.cursor()

# Insert some sample data
cur.execute("""
    INSERT INTO mytable (name) VALUES ('Alice'), ('Bob'), ('Charlie')
""")

# Commit the transaction
conn.commit()

# Verify that the data exists
cur.execute("SELECT * FROM mytable")
rows = cur.fetchall()

if len(rows) == 0:
    print("No data found in mytable")
else:
    for row in rows:
        print(row)

# Close the cursor and connection
cur.close()
conn.close()
