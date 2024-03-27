import numpy as np
from flask import Flask, render_template, request 
import os
from datetime import datetime
import sqlite3
import pandas as pd


app = Flask(__name__) 
connect = sqlite3.connect('database.db')
connect.execute('CREATE TABLE IF NOT EXISTS USER (name TEXT,  email TEXT, password TEXT)')
connect.execute('CREATE TABLE IF NOT EXISTS ADMIN (email TEXT, passward TEXT)')

@app.route('/') 
@app.route('/home') 
def index():
	return render_template('index.html') 

    
    
# if request.method == 'POST': 
# 	email=request.form['email']
# 	passward=request.form['passward']
# 	emails=['ds1083@srmist.eud.in','vs33@srmist.edu.in']
# 	passwards=['123456','123456']
# 	connect = sqlite3.connect('database.db') 
# 	# 	cursor = connect.cursor() 
# 	# 	cursor.execute('SELECT * FROM PARTICIPANTS1') 
# 	# 	data = cursor.fetchall() 
# 	# 	return render_template("Registration_details.html", data=data)
# 	if email in emails:
# 		if passward==passwards[emails.index(email)]:
		
# 			return render_template("user_dashboard.html") 
# 		else:
# 			return render_template('signin.html')
# else:
# 	return render_template('signin.html') 




@app.route('/signin',methods=["POST",'GET']) 
def signin():
    if request.method == 'POST':
        
        email=request.form['email']
        password=request.form['password']
        # emails=['devan333s@gmail.com']
        passwords=['123456','123456']
        admin=['ds1083@srmist.edu.in','vs33@srmist.edu.in']
        if email in admin:
            return render_template('upload.html')
        # if email in emails:
            # if password==passwords[emails.index(email)]:
        
        else:
            data=retrive_data(email)
            print(data)
            return render_template("user_dashboard.html",data=data)
        #     else:
        #         return "Please, Check your password!"
        # else:
        #     return "Please, Check your email and password!"
    else:
        return render_template('signin.html')
        
        
def retrive_data(email):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    names = cursor.fetchall()

    detials=[]
    for name in names:
        table_name = name[0]
        

        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        # print(rows)
        df = pd.DataFrame(rows, columns=["Name", "Register_number", "Event", "Email"])
        data=[i for i in df.values]
        for i in range(len(data)):
            detials.append(data[i])
    

    
    df=pd.DataFrame(detials,columns=["Name", "Register_number", "Event", "Email"])
    # print(df)
    dataframe=df[df['Email']==email]
    print(dataframe)
    final_data=[]
    data_=[i for i in dataframe.values]
    for i in range(len(data_)):
        final_data.append(data_[i])
    return final_data

    
    
    # conn = sqlite3.connect('data.db')
    # cursor = conn.cursor()
    # cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    # names = cursor.fetchall()
    # detials=[]
    # for name in names:
    #     table_name = name[0]
    #     cursor.execute(f"SELECT * FROM {table_name}")
    #     rows = cursor.fetchall()
    #     df = pd.DataFrame(rows, columns=["Name", "Register_number", "Event", "Email"])
    #     data=[i for i in df.values]
    #     for i in range(len(data)):
    #         detials.append(data[i])
    # # df=pd.DataFrame(detials,columns=["Name", "Register_number", "Event", "Email"])
    # # print(df)
    # # Close the cursor and connection outside the loop

    # cursor.close()
    # conn.close()
    # print(detials)
    # return detials




@app.route('/signup',methods=['GET','POST']) 
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email= request.form['email']
        password = request.form['password']
        with sqlite3.connect("database.db") as users:
            cursor = users.cursor()
            cursor.execute("INSERT INTO USER(name,email,password) VALUES (?,?,?)", (name, email,password))
            users.commit()
            
        return render_template('signin.html')
    else:
        return render_template('signup.html')


# @app.route('/admin', methods=['GET', 'POST']) 
# def admin(): 
	
# 		return render_template('admin.html') 


# @app.route('/Registration_details') 
# def participants(): 
# 	connect = sqlite3.connect('database.db') 
# 	cursor = connect.cursor() 
# 	cursor.execute('SELECT * FROM PARTICIPANTS1') 
# 	data = cursor.fetchall() 
# 	return render_template("Registration_details.html", data=data) 





@app.route('/user_dashboard',methods=["POST","GET"])
def user_dashboard():
    if request.method == 'POST':
        return render_template("user_dashboard.html")
    else:
        return render_template('signin.html') 

  

    
# connect = sqlite3.connect('database.db') 
	# 	cursor = connect.cursor() 
	# 	cursor.execute('SELECT * FROM PARTICIPANTS1') 
	# 	data = cursor.fetchall() 
	# 	return render_template("Registration_details.html", data=data)
# 	email=request.form['email']
# 	password=request.form['password']
# 	emails=['ds1083@srmist.eud.in','vs33@srmist.edu.in']
# 	passwords=['123456','123456']
# 	connect = sqlite3.connect('database.db') 
# 	# 	cursor = connect.cursor() 
# 	# 	cursor.execute('SELECT * FROM PARTICIPANTS1') 
# 	# 	data = cursor.fetchall() 
# 	# 	return render_template("Registration_details.html", data=data)
# 	if email in emails:
# 		if password==passwords[emails.index(email)]:
		
# 			return render_template("user_dashboard.html") 
# 		else:
# 			return render_template('signin.html')

# Configuration for SQLite database
DB_NAME = 'data.db'

# List to store table names
db_name_list = []

# Check if database exists, if not create it
if not os.path.exists(DB_NAME):
    conn = sqlite3.connect(DB_NAME)
    conn.close()

@app.route('/admin')
def admin():
    return render_template('upload.html')


@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "No file part"

    file = request.files['file']
    
    if file.filename == '':
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
        
       
        return f"File uploaded successfully and data inserted into table: {table_name}"

    return "Error occurred while uploading file."


def admin_retrive_data():
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











if __name__ == '__main__':
    app.run(debug=True)
















if __name__ == '__main__': 
	app.run(debug=True) 



