import sqlite3

# Establish a connection to the SQLite database
conn = sqlite3.connect('mydata.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Execute a SQL query
cursor.execute('SELECT * FROM mytable')

# Fetch one row at a time and print the results
for row in cursor.fetchall():
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()