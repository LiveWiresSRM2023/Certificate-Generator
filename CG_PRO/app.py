



from flask import Flask, render_template, request 
import sqlite3 


app = Flask(__name__) 


@app.route('/certificate_dow') 
def certi_dow(): 
	return render_template('certificate_dow.html') 


@app.route('/') 
@app.route('/home') 
def index(): 
	return render_template('index.html') 


connect = sqlite3.connect('database.db') 
connect.execute('CREATE TABLE IF NOT EXISTS PARTICIPANTS1 (name TEXT,  email TEXT, city TEXT, country TEXT, phone TEXT)') 
connect.execute('CREATE TABLE IF NOT EXISTS ADMIN (email TEXT, password TEXT)') 



@app.route('/signin') 
def signin(): 
	return render_template('signin.html') 


@app.route('/signup') 
def signup(): 
	return render_template('signup.html') 


@app.route('/register', methods=['GET', 'POST']) 
def register(): 
	if request.method == 'POST': 
		name = request.form['name'] 
		email= request.form['email'] 
		city = request.form['city'] 
		country = request.form['country'] 
		phone = request.form['phone'] 
		
		# if email in emails:
		# 	pass

		with sqlite3.connect("database.db") as users: 
			cursor = users.cursor() 
			cursor.execute("INSERT INTO PARTICIPANTS1  (name,email,city,country,phone) VALUES (?,?,?,?,?)", (name, email, city, country, phone)) 
			users.commit() 
		return render_template("certificate_dow.html") 
	else: 
		return render_template('register.html') 



@app.route('/admin_login', methods=['GET', 'POST']) 
def admin_login(): 
	if request.method == 'POST': 
		emails=['ds1083@srmist.edu.in']
		email = request.form['email']
		password = request.form['password']
		if email in emails:
			return render_template("admin.html") 
		else:
			return 'Please enter correct email id'

	else:
		
		return render_template('admin_login.html') 


@app.route('/Registration_details') 
def participants(): 
	connect = sqlite3.connect('database.db') 
	cursor = connect.cursor() 
	cursor.execute('SELECT * FROM PARTICIPANTS1') 
	data = cursor.fetchall() 
	return render_template("Registration_details.html", data=data) 






if __name__ == '__main__': 
	app.run(debug=True) 



