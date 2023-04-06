import psycopg2

# Set up a connection to the database
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="punkinbunker"
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
