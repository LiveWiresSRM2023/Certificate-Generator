from flask import Flask, render_template, request
import pandas as pd
import sqlite3
import os
from datetime import datetime

app = Flask(__name__)

# Configuration for SQLite database
DB_NAME = 'data.db'
temp_name = "ppt_temp"

# List to store table names
db_name_list = []

# Check if database exists, if not create it
if not os.path.exists(DB_NAME):
    conn = sqlite3.connect(DB_NAME)
    conn.close()

if not os.path.exists(temp_name):
    os.makedirs(temp_name)
    
    
@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "No file part"
    
    if 'ppt_file' not in request.files:
        return "no template uploaded yet!!"

    file = request.files['file']
    ppt = request.files['ppt_file']
    
    
    if file.filename == '' or ppt.filename == '':
        return "No selected file"

    if file:
        # Read Excel file
        df = pd.read_excel(file)
        
        # Connect to SQLite database
        conn = sqlite3.connect(DB_NAME)

        # Generate a unique table name based on current timestamp
        table_name = f"data_table_{datetime.now().strftime('%Y%m%d%H%M%S')}"

        # Insert data into SQLite database with the generated table name
        df.to_sql(table_name, conn, if_exists='replace', index=False)

        # Append the table name to the list
        db_name_list.append(table_name)

        # Commit and close connection
        conn.commit()
        conn.close()
        
        if ppt:
            ppt.save(os.path.join(temp_name, ppt.filename))

        return f"File uploaded successfully and data inserted into table: {table_name}"

    return "Error occurred while uploading file."
    
   

if __name__ == '__main__':
    app.run(debug=True)
