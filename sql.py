# Module Imports
import mariadb
import sys

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="erinpy",
        password="tendercode",
        host="192.168.111.235",
        port=3306,
        database="ustenders"
    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()

# SQL Query to execute
query = "SELECT * FROM rss_tenders rt WHERE rt.pdflinks != '[]'"

# Execute the query
try:
    cur.execute(query)
    # Fetch all results from the executed query
    results = cur.fetchall()

    # Print the column names
    column_names = [desc[0] for desc in cur.description]
    print(f"Columns: {', '.join(column_names)}")

    # Print each row
    for row in results:
        print(row)
except mariadb.Error as e:
    print(f"Error: {e}")

# Close the connection
conn.close()

