import sqlite3
import pandas as pd
# from upload import db_name_list

# # Iterate over db_name_list and print each item
# for table_name in db_name_list:
#     print(table_name)


# Connect to SQLite database
conn = sqlite3.connect('data.db')

# Create a cursor object
cursor = conn.cursor()


# execute this query to fetch the table names
# cursor.execute("SELECT name from sqlite_master WHERE type='table';")
# names = cursor.fetchall()
# for i in names:
#     print("Tables_name: ",i[0])
    
# cursor.close()
# conn.close()

# cursor = conn.cursor()
cursor.execute("SELECT name from sqlite_master WHERE type='table';")
names = cursor.fetchall()
for i in names:
    # print("Tables_name: ",i[0])

# Execute SELECT query to fetch data
    cursor.execute(f"SELECT * FROM {i[0]}")

# Fetch all rows
    rows = cursor.fetchall()

# Close cursor and connection
    # cursor.close()
    # conn.close()

# Convert fetched data into DataFrame
    df = pd.DataFrame(rows, columns=["name","section"])

# Print DataFrame
    print(df)
cursor.close()
conn.close()