from flask import Flask, render_template, request, session
import random





from flask import Flask


app = Flask(__name__)
app.debug=True

@app.route('/')

def hello_world():
    return render_template('user_dashboard.html')












# @app.route('/sign_in',methods=['GET','POST'])
# def sign_in():
#     if request.method == 'POST': 
# 		# emails=['ds1083@srmist.edu.in']
# 		df=df=pd.DataFrame(pd.read_excel("C:/Users/Dev/Desktop/Live_wires_project/Certificate-Generator/front-end/User_Dashboard/paticipent_data.xlsx" ))
# 		emails=df['email']
#     	# return render_template('main.html')
     
# 		email = request.form['email']
# 		password = request.form['password']
# 		data=df[df['email']=='devan333s@gmail.com']

# 		df=pd.DataFrame(pd.read_excel("C:/Users/Dev/Desktop/Live_wires_project/Certificate-Generator/front-end/User_Dashboard/paticipent_data.xlsx" ))
# 		posted_email='devan333s@gmail.com'
# 		name=[i for i in df[df['email']==posted_email]['Name']]
# 		reg=[i for i in df[df['email']==posted_email]['Register number']]
# 		evant=[ i for i in df[df['email']==posted_email]['evant']]
# 		email=[i for i in df[df['email']==posted_email]['email']]
# 		data=[]
# 		for i in range(0,len(name)):
# 			data.append([name[i],reg[i],evant[i],email[i]])
			
  
  
# 		if email in emails:
# 			return render_template("main.html",data) 
# 		else:
# 			return 'Please enter correct email id'

# 	else:
		
# 		return render_template('signin.html')
    

# import pandas as pd
# @app.route('/user_dashboard') 
# def user_dashboard():
    
#     df=pd.read_excel('paticipent_data.xlsx')
#     print(df)
#     return render_template('main.html')
    


	


if __name__ == '__main__':

	
	app.run()



