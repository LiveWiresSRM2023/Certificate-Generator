from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = 'Rajeshk1006'

@app.route("/")
def home():
    return render_template("mobile.html")

@app.route("/front-end/otpverification/templates/getph", methods=['POST'])
def get_ph():
    num = request.form['number']
    return num  # Or render another template for failure

# authen


if __name__ == '__main__': 
	app.run(debug=True) 

