# Module Imports
import mariadb
import sys

def sql_main():
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
    query = "SELECT pdflinks FROM rss_tenders rt WHERE rt.pdflinks != '[]'"

    # Execute the query
    try:
        cur.execute(query)
        # Fetch all results from the executed query
        results = cur.fetchall()
        # Process and return the results as a list of URLs
        pdf_urls = [row[0] for row in results]
        return pdf_urls        

    except mariadb.Error as e:
        print(f"Error: {e}")
        return []

    finally:
        # Close the connection
        conn.close()

# Example usage
if __name__ == "__main__":
    pdf_urls = sql_main()
    print(pdf_urls)
