from flask import render_template
from flask import url_for, redirect
# Import Request object to use
from flask import request
# from sqlalchemy import and_
from flask import url_for, redirect, request, make_response,flash
# Importing Session Object to use Sessions
from flask import session
# from app.models import User
from app import app , db
from app.models import User
from sqlalchemy import and_

@app.route('/')
@app.route('/index')
def index():
	if 'user' in session:
		return render_template('index.html', logged_in = True)
	else:
		return render_template('index.html', logged_in = False)



@app.route('/login', methods=['POST', 'GET'])
def User_Login():
    userID = request.form['user']
    psswd = request.form['pass']
    user  = User.query.filter(and_(User.username == userID, User.password == psswd)).first()
    if user:
        flash('Login successful', 'success')
        session['user'] = userID
        return render_template('User_HomePage.html', username=session['user'], logged_in = True)
    return render_template("index.html", logged_in = False)

@app.route('/logout', methods=['POST', 'GET'])
def Logout():
	if 'user' in session:
		name = session.pop('user')
		return render_template("index.html", logged_in = False)

	else:
		return render_template("index.html")

@app.route('/userpage',methods=['POST'])
def User_HomePage():
    # user = User(username=request.form["username"],  password=request.form['newpass'], email=request.form["email"],)
    # db.session.add(user)
    # db.session.commit()
    # flash('Your account has been created! You are now able to log in', 'success')
    return render_template('User_HomePage.html', logged_in=True, username=session['user'])

@app.route('/qanda',methods=['POST', 'GET'])
def QandA():
    if 'user' in session:
	    return render_template('QandA.html', logged_in = True, username = session['user'])
    else:
	    return render_template('QandA.html', logged_in = False)

@app.route('/askques',methods=['POST','GET'])
def Ask_Question():
	return render_template('Ask_Ques.html')

@app.route('/about')
def About():
	return render_template('About.html')

@app.route('/coc')
def Answering_Policy():
	return render_template('Answering_Policy.html')





