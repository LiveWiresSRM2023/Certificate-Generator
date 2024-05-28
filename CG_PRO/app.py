import random
import smtplib
import numpy as np
from flask import Flask, render_template, request 
import os
from datetime import datetime
import sqlite3
import pandas as pd
from generator_engine.demo import gen_engine
from flask import send_from_directory


app = Flask(__name__) 
connect = sqlite3.connect('database.db')
connect.execute('CREATE TABLE IF NOT EXISTS USER (name TEXT,  email TEXT, password TEXT)')
connect.execute('CREATE TABLE IF NOT EXISTS ADMIN (email TEXT, passward TEXT)')
OTP=""
receiver_email=""
user_name=""
@app.route('/') 
@app.route('/home') 
def index():
	return render_template('index.html') 


@app.route('/download')
def download_file():
    filename = request.args.get('filename')
    directory = "C:\\Users\\Dev\\Desktop\\Certificate-Generator\\CG_PRO\\generator_engine"
    return send_from_directory(directory, filename, as_attachment=True)


@app.route('/signin',methods=["POST",'GET']) 
def signin():
    if request.method == 'POST':
        
        email=request.form['email']
        password=request.form['password']
        
        admin=['ds1083@srmist.edu.in','vs33@srmist.edu.in']
        if email in admin:
            return render_template('upload.html')
        
        connect = sqlite3.connect('database.db')
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM USER ;")
        data_= cursor.fetchall()
        def check_email(data_):
            for i in data_:
                if ((i[1]==email) and (i[2]==password)):
                    return True
            else:
                return False
        if check_email(data_):

            data=retrive_data(email)
            names=[i[0] for i in data]
            engine = gen_engine()
            # Call the generate method with the list of names
            engine.generate( {'Name': names})

            
            return render_template("user_dashboard.html",data=data)
        else:
            return "Please, Check your email and password!"
    else:
        return render_template('signin.html')
        
        

        # names = {'Name': ['Rajesh k', "Mohammad Vaseem", "Devan S", "Nikil Paul", "Saravana Kumar"]}




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
        df = pd.DataFrame(rows, columns=["Name", "Register_number", "Event", "Email"])
        print(df)
        data=[i for i in df.values]
        for i in range(len(data)):
            detials.append(data[i])
    df=pd.DataFrame(detials,columns=["Name", "Register_number", "Event", "Email"])
    dataframe=df[df['Email']==email]
    print(dataframe)
    final_data=[]
    data_=[i for i in dataframe.values]
    for i in range(len(data_)):
        final_data.append(data_[i])
    return final_data

@app.route('/signup',methods=['GET','POST']) 
def signup():
    global receiver_email
    global user_name
    if request.method == 'POST':
        name = request.form['name']
        email= request.form['email']
        receiver_email=email
        user_name=name
        password = request.form['password']
        with sqlite3.connect("database.db") as users:
            cursor = users.cursor()
            cursor.execute("INSERT INTO USER(name,email,password) VALUES (?,?,?)", (name, email,password))
            users.commit()
        otp()
        return render_template('otp.html')
    else:
        return render_template('signup.html')


@app.route('/user_dashboard',methods=["POST","GET"])
def user_dashboard():
    if request.method == 'POST':
        return render_template("user_dashboard.html")
    else:
        return render_template('signin.html') 


DB_NAME = 'data.db'
db_name_list = []
if not os.path.exists(DB_NAME):
    conn = sqlite3.connect(DB_NAME)
    conn.close()

@app.route('/admin')
def admin(a=True):
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "No file part"
    file = request.files['file']
    if file.filename == '':
        return "No selected file"
    if file:
        df = pd.read_excel(file)
        conn = sqlite3.connect(DB_NAME)
        table_name = f"data_table_{datetime.now().strftime('%Y%m%d%H%M%S')}"
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        db_name_list.append(table_name)
        conn.commit()
        conn.close()
        return f"File uploaded successfully and data inserted into table: {table_name}"
    return "Error occurred while uploading file."


def otp():
    global OTP

    
    OTP = random.randint(100000,999999)      #generating a randomm 6-digit OTP

    #setting up server
    server = smtplib.SMTP('smtp.gmail.com',587)
    #server = smtplib.SMTP('64.233.184.108',587)           #IP address of smtp.gmail.com to bypass DNS resolution
    server.starttls()

    # name = input("enter your name:")
    global receiver_email
    global user_name
    name=user_name
    # receiver_email = input("enter ur email id:")

    def email_verification(receiver_email):
        email_check1 = ["gmail","hotmail","yahoo","outlook"]
        email_check2 = [".com",".in",".org",".edu",".co.in"]
        count = 0

        for domain in email_check1:
            if domain in receiver_email:
                count+=1
        for site in email_check2:
            if site in receiver_email:
                count+=1

        if "@" not in receiver_email or count!=2:
            print("invalid email id")
            new_receiver_email = input("enter correct email id:")
            email_verification(new_receiver_email)
            return new_receiver_email
        
        return receiver_email

    valid_receiver_email = email_verification(receiver_email)
    password = "stqqwjqoocucknsx"
    server.login("priyanshu25122002@gmail.com",password)


    body = "dear"+name+","+"\n"+"\n"+"your OTP is "+str(OTP)+"."
    subject = "OTP verification using python"
    message = f'subject:{subject}\n\n{body}'

    server.sendmail("priyanshu25122002@gmail.com",valid_receiver_email,message)





    

    def sending_otp(receiver_email):
        new_otp = random.randint(100000,999999)

        body = "dear"+name+","+"\n"+"\n"+"your OTP is "+str(new_otp)+"."
        subject = "OTP verification using python" 
        message = f'subject:{subject}\n\n{body}'
        server.sendmail("priyanshu25122002@gmail.com",receiver_email,message)
        print("OTP has been sent to"+receiver_email)
        received_OTP = int(input("enter OTP:"))

        if received_OTP==new_otp:
            return("OTP verified")
        else:
            sending_otp(receiver_email)
            return("invalid OTP")
            
            
        
    print("OTP has been sent to "+valid_receiver_email)
    
    


def admin_retrive_data():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name from sqlite_master WHERE type='table';")
    names = cursor.fetchall()
    for i in names:
        cursor.execute(f"SELECT * FROM {i[0]}")
        rows = cursor.fetchall()
        df = pd.DataFrame(rows, columns=["name","section"])
    cursor.close()
    conn.close()

@app.route('/otp_verify',methods=["POST"])
def otp_verfication():


    global OTP
    if request.method == 'POST':
        received_OTP = request.form['OTP']

        if int(received_OTP)==int(OTP):
            print("OTP verified")
            return render_template('signin.html')
            
        else:
            print(OTP,received_OTP)
            return("invalid OTP")
            # answer = input("enter yes to resend OTP on same email and no to enter a new email id:")
            # YES = ['YES','yes','Yes']
            # NO = ['NO','no','No']
            # if answer in YES:
            #     sending_otp(valid_receiver_email)
            # elif answer in NO:
            #     new_receiver_email = input("enter new email id:")
            #     email_verification(new_receiver_email)
            #     sending_otp(new_receiver_email)
            # else:
                # print("invalid input")

        server.quit()
        



if __name__ == '__main__':
    app.run(debug=True)
























# from flask import Flask, render_template
# from generator_engine.demo import gen_engine

# app = Flask(__name__)

# # Create an instance of the gen_engine class


# @app.route('/admin')
# def admin():
#     # Define the list of names
#     names = {'Name': ['Rajesh k', "Mohammad Vaseem", "Devan S", "Nikil Paul", "Saravana Kumar"]}
#     engine = gen_engine()
#     # Call the generate method with the list of names
#     engine.generate(names)
    
#     return render_template('upload.html')

# if __name__ == "__main__":
#     # app.run(debug=True)
#     app.run(port=5001)
