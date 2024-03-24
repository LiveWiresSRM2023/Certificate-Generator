



from flask import Flask, render_template, request 
import sqlite3 


app = Flask(__name__) 
connect = sqlite3.connect('database.db')
connect.execute('CREATE TABLE IF NOT EXISTS USER (name TEXT,  email TEXT, password TEXT)')
connect.execute('CREATE TABLE IF NOT EXISTS ADMIN (email TEXT, passward TEXT)')

@app.route('/') 
@app.route('/home') 
def index():
	return render_template('signin.html') 

    
    
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
        emails=['devan333s@gmail.com']
        passwords=['123456','123456']
        admin=['ds1083@srmist.edu.in','vs33@srmist.edu.in']
        if email in admin:
            return render_template('admin.html')
        if email in emails:
            if password==passwords[emails.index(email)]:
                return render_template("user_dashboard.html")
            else:
                return "Please, Check your password!"
        else:
            return "Please, Check your email and password!"
    else:
        return render_template('signin.html')
        


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


@app.route('/admin', methods=['GET', 'POST']) 
def admin(): 
	
		return render_template('admin.html') 


# @app.route('/Registration_details') 
# def participants(): 
# 	connect = sqlite3.connect('database.db') 
# 	cursor = connect.cursor() 
# 	cursor.execute('SELECT * FROM PARTICIPANTS1') 
# 	data = cursor.fetchall() 
# 	return render_template("Registration_details.html", data=data) 



# @app.route('/d')
# def 

# if request.method == 'POST':

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









if __name__ == '__main__': 
	app.run(debug=True) 



