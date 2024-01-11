import sqlite3

# Connect to the database
conn = sqlite3.connect('Chinook.db')

# Get a cursor
cursor = conn.cursor()

# Query the database
cursor.execute("SELECT * FROM table_name")

# Fetch the results
results = cursor.fetchall() 

# Close the connection
conn.close()