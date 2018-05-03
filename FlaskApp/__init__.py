# -*- coding: utf-8 -*
from flask import Flask, render_template, flash, request, url_for,redirect, session
from  content_management_system import CS_Content, ATL_Content
from dbconn import connection
from wtforms import Form, BooleanField, TextField, PasswordField, validators
from passlib.hash import  sha256_crypt
from MySQLdb import escape_string as thwart
from functools import wraps
import gc
import os
import smtplib
#import sys
#reload(sys)
#sys.setdefaultencoding('utf8') 
from flask_mail import Mail, Message

#context = SSL.Context(SSL.SSLv23_METHOD)
#context.use_privatekey_file('/etc/apache2/ssl/apache.key')
#context.use_certificate_file('/etc/apache2/ssl/apache.crt')
TOPIC_DICT = CS_Content()
TOPIC_DICT_articles = ATL_Content()

app = Flask(__name__)

#app.config.update(
#	DEBUG=True,
#	#EMAIL SETTINGS
#	MAIL_SERVER='smtp.gmail.com',
#	MAIL_PORT=465,
#	MAIL_USE_SSL=True,
#	MAIL_USERNAME = 'jak2013jak@gmail.com',
#	MAIL_PASSWORD = 'fengjun3426119'
#		)
app.config.update(
                  DEBUG=True,
                  #EMAIL SETTINGS
                  MAIL_SERVER='smtp.qq.com',
                  MAIL_PORT=465,
                  MAIL_USE_SSL=True,
                  MAIL_USERNAME = '103886415',
                  MAIL_PASSWORD = 'hbawxncxckmcbhie'
                  )
mail = Mail(app)

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
	try:
        	if 'logged_in' in session:
            		return f(*args, **kwargs)
        	else:
            		flash("You need to login first")
            		return redirect(url_for('login'))
	except Exception as e:
		return str(e)
    return wrap

@app.route("/")
def homepage():
    return render_template("main.html")
    #return render_template("test.html")

@app.route("/dashboard/", methods=['GET','POST'])
def dashboard():
	try:
		try:
			client_name, settings, tracking, rank = user_info()
			if len(tracking)<10:
				tracking = "/introductions/"
			gc.collect()
			if client_name=="Guest":
				flash("Welcome Guest, no progress tracking")
				tracking=['None']
			update_user_tracking()
			completed_percentages = topic_completion_percent()
			return render_template("dashboard.html", TOPIC_DICT = TOPIC_DICT,TOPIC_DICT_articles=TOPIC_DICT_articles).encode( "utf-8" )
    			
		except:
			return render_template("dashboard.html", TOPIC_DICT = TOPIC_DICT,TOPIC_DICT_articles=TOPIC_DICT_articles).encode( "utf-8" )
	except Exception as e:
		return (str(e))



@app.route(TOPIC_DICT_articles["Foods"][0][1], methods=['GET', 'POST'])
def coffe_introduction():
    lastnum=len(TOPIC_DICT_articles["Foods"])-1
    try:
        if lastnum>0:
            update_user_tracking()
            completed_percentages = topic_completion_percent()
            return render_template("articles/Foods/coffe-introduction.html",completed_percentages=completed_percentages, curLink = TOPIC_DICT_articles["Foods"][0][1], curTitle=TOPIC_DICT_articles["Foods"][0][0],  nextLink = TOPIC_DICT_articles["Foods"][1][1], nextTitle = TOPIC_DICT_articles["Foods"][1][0],TOPIC_DICT_articles=TOPIC_DICT_articles)
        else:
            update_user_tracking()
            completed_percentages = topic_completion_percent()
            return render_template("articles/Foods/coffe-introduction.html",completed_percentages=completed_percentages, curLink = TOPIC_DICT_articles["Foods"][0][1], curTitle=TOPIC_DICT_articles["Foods"][0][0],  nextLink = "", nextTitle = "",TOPIC_DICT_articles=TOPIC_DICT_articles)
    except Exception as e:
        return (str(e))



@app.route(TOPIC_DICT_articles["Foods"][1][1], methods=['GET', 'POST'])
def coffe_history():
    lastnum=len(TOPIC_DICT_articles["Foods"])-1
    try:
        if lastnum>1:
            update_user_tracking()
            completed_percentages = topic_completion_percent()
            return render_template("articles/Foods/coffe-history.html",completed_percentages=completed_percentages, curLink = TOPIC_DICT_articles["Foods"][1][1], curTitle=TOPIC_DICT_articles["Foods"][1][0],  nextLink = TOPIC_DICT_articles["Foods"][2][1], nextTitle = TOPIC_DICT_articles["Foods"][2][0],TOPIC_DICT_articles=TOPIC_DICT_articles)
        else:
            update_user_tracking()
            completed_percentages = topic_completion_percent()
            return render_template("articles/Foods/coffe-history.html",completed_percentages=completed_percentages, curLink = TOPIC_DICT_articles["Foods"][1][1], curTitle=TOPIC_DICT_articles["Foods"][1][0],  nextLink = "", nextTitle = "",TOPIC_DICT_articles=TOPIC_DICT_articles)
    except Exception as e:
        return (str(e))



@app.route(TOPIC_DICT_articles["Family Activities"][0][1], methods=['GET', 'POST'])
def go_to_Shanghai_Zoo():
    lastnum=len(TOPIC_DICT_articles["Family Activities"])-1
    try:
        if lastnum>0:
            update_user_tracking()
            completed_percentages = topic_completion_percent()
            return render_template("articles/Family Activities/go-to-Shanghai-Zoo.html",completed_percentages=completed_percentages, curLink = TOPIC_DICT_articles["Family Activities"][0][1], curTitle=TOPIC_DICT_articles["Family Activities"][0][0],  nextLink = TOPIC_DICT_articles["Family Activities"][1][1], nextTitle = TOPIC_DICT_articles["Family Activities"][1][0],TOPIC_DICT_articles=TOPIC_DICT_articles)
        else:
            update_user_tracking()
            completed_percentages = topic_completion_percent()
            return render_template("articles/Family Activities/go-to-Shanghai-Zoo.html",completed_percentages=completed_percentages, curLink = TOPIC_DICT_articles["Family Activities"][0][1], curTitle=TOPIC_DICT_articles["Family Activities"][0][0],  nextLink = "", nextTitle = "",TOPIC_DICT_articles=TOPIC_DICT_articles)
    except Exception as e:
        return (str(e))



@app.route(TOPIC_DICT_articles["Traveling"][0][1], methods=['GET', 'POST'])
def Bali_vacation():
    lastnum=len(TOPIC_DICT_articles["Traveling"])-1
    try:
        if lastnum>0:
            update_user_tracking()
            completed_percentages = topic_completion_percent()
            return render_template("articles/Traveling/Bali-vacation.html",completed_percentages=completed_percentages, curLink = TOPIC_DICT_articles["Traveling"][0][1], curTitle=TOPIC_DICT_articles["Traveling"][0][0],  nextLink = TOPIC_DICT_articles["Traveling"][1][1], nextTitle = TOPIC_DICT_articles["Traveling"][1][0],TOPIC_DICT_articles=TOPIC_DICT_articles)
        else:
            update_user_tracking()
            completed_percentages = topic_completion_percent()
            return render_template("articles/Traveling/Bali-vacation.html",completed_percentages=completed_percentages, curLink = TOPIC_DICT_articles["Traveling"][0][1], curTitle=TOPIC_DICT_articles["Traveling"][0][0],  nextLink = "", nextTitle = "",TOPIC_DICT_articles=TOPIC_DICT_articles)
    except Exception as e:
        return (str(e))



@app.route(TOPIC_DICT_articles["Traveling"][1][1], methods=['GET', 'POST'])
def ThaiLand():
    lastnum=len(TOPIC_DICT_articles["Traveling"])-1
    try:
        if lastnum>1:
            update_user_tracking()
            completed_percentages = topic_completion_percent()
            return render_template("articles/Traveling/ThaiLand.html",completed_percentages=completed_percentages, curLink = TOPIC_DICT_articles["Traveling"][1][1], curTitle=TOPIC_DICT_articles["Traveling"][1][0],  nextLink = TOPIC_DICT_articles["Traveling"][2][1], nextTitle = TOPIC_DICT_articles["Traveling"][2][0],TOPIC_DICT_articles=TOPIC_DICT_articles)
        else:
            update_user_tracking()
            completed_percentages = topic_completion_percent()
            return render_template("articles/Traveling/ThaiLand.html",completed_percentages=completed_percentages, curLink = TOPIC_DICT_articles["Traveling"][1][1], curTitle=TOPIC_DICT_articles["Traveling"][1][0],  nextLink = "", nextTitle = "",TOPIC_DICT_articles=TOPIC_DICT_articles)
    except Exception as e:
        return (str(e))



@app.route(TOPIC_DICT_articles["Kids"][0][1], methods=['GET', 'POST'])
def pre_school_learning():
    lastnum=len(TOPIC_DICT_articles["Kids"])-1
    try:
        if lastnum>0:
            update_user_tracking()
            completed_percentages = topic_completion_percent()
            return render_template("articles/Kids/pre-school-learning.html",completed_percentages=completed_percentages, curLink = TOPIC_DICT_articles["Kids"][0][1], curTitle=TOPIC_DICT_articles["Kids"][0][0],  nextLink = TOPIC_DICT_articles["Kids"][1][1], nextTitle = TOPIC_DICT_articles["Kids"][1][0],TOPIC_DICT_articles=TOPIC_DICT_articles)
        else:
            update_user_tracking()
            completed_percentages = topic_completion_percent()
            return render_template("articles/Kids/pre-school-learning.html",completed_percentages=completed_percentages, curLink = TOPIC_DICT_articles["Kids"][0][1], curTitle=TOPIC_DICT_articles["Kids"][0][0],  nextLink = "", nextTitle = "",TOPIC_DICT_articles=TOPIC_DICT_articles)
    except Exception as e:
        return (str(e))



@app.route(TOPIC_DICT_articles["Kids"][1][1], methods=['GET', 'POST'])
def balance_between_school_and_home():
    lastnum=len(TOPIC_DICT_articles["Kids"])-1
    try:
        if lastnum>1:
            update_user_tracking()
            completed_percentages = topic_completion_percent()
            return render_template("articles/Kids/balance-between-school-and-home.html",completed_percentages=completed_percentages, curLink = TOPIC_DICT_articles["Kids"][1][1], curTitle=TOPIC_DICT_articles["Kids"][1][0],  nextLink = TOPIC_DICT_articles["Kids"][2][1], nextTitle = TOPIC_DICT_articles["Kids"][2][0],TOPIC_DICT_articles=TOPIC_DICT_articles)
        else:
            update_user_tracking()
            completed_percentages = topic_completion_percent()
            return render_template("articles/Kids/balance-between-school-and-home.html",completed_percentages=completed_percentages, curLink = TOPIC_DICT_articles["Kids"][1][1], curTitle=TOPIC_DICT_articles["Kids"][1][0],  nextLink = "", nextTitle = "",TOPIC_DICT_articles=TOPIC_DICT_articles)
    except Exception as e:
        return (str(e))

@app.route(TOPIC_DICT["SQLite"][0][1], methods=['GET', 'POST'])
@login_required
def Inserting_into_a_Database_with_SQLite():
    lastnum=len(TOPIC_DICT["SQLite"])-1
    try:
        if lastnum>0:
            update_user_tracking()
            completed_percentages = topic_completion_percent()
            return render_template("tutorials/SQLite/sql-database-python-part-1-inserting-database.html",completed_percentages=completed_percentages, curLink = TOPIC_DICT["SQLite"][0][1], curTitle=TOPIC_DICT["SQLite"][0][0],  nextLink = TOPIC_DICT["SQLite"][1][1], nextTitle = TOPIC_DICT["SQLite"][1][0],TOPIC_DICT=TOPIC_DICT)
        else:
            update_user_tracking()
            completed_percentages = topic_completion_percent()
            return render_template("tutorials/SQLite/sql-database-python-part-1-inserting-database.html",completed_percentages=completed_percentages, curLink = TOPIC_DICT["SQLite"][0][1], curTitle=TOPIC_DICT["SQLite"][0][0],  nextLink = "", nextTitle = "",TOPIC_DICT=TOPIC_DICT)
    except Exception as e:
        return (str(e))



@app.route(TOPIC_DICT["SQLite"][1][1], methods=['GET', 'POST'])
def Dynamically_Inserting_into_a_Database_with_SQLite():
    lastnum=len(TOPIC_DICT["SQLite"])-1
    try:
        if lastnum>1:
            update_user_tracking()
            completed_percentages = topic_completion_percent()
            return render_template("tutorials/SQLite/sqlite-part-2-dynamically-inserting-database-timestamps.html",completed_percentages=completed_percentages, curLink = TOPIC_DICT["SQLite"][1][1], curTitle=TOPIC_DICT["SQLite"][1][0],  nextLink = TOPIC_DICT["SQLite"][2][1], nextTitle = TOPIC_DICT["SQLite"][2][0],TOPIC_DICT=TOPIC_DICT)
        else:
            update_user_tracking()
            completed_percentages = topic_completion_percent()
            return render_template("tutorials/SQLite/sqlite-part-2-dynamically-inserting-database-timestamps.html",completed_percentages=completed_percentages, curLink = TOPIC_DICT["SQLite"][1][1], curTitle=TOPIC_DICT["SQLite"][1][0],  nextLink = "", nextTitle = "",TOPIC_DICT=TOPIC_DICT)
    except Exception as e:
        return (str(e))



@app.route(TOPIC_DICT["SQLite"][2][1], methods=['GET', 'POST'])
def Read_from_Database_with_SQLite():
    lastnum=len(TOPIC_DICT["SQLite"])-1
    try:
        if lastnum>2:
            update_user_tracking()
            completed_percentages = topic_completion_percent()
            return render_template("tutorials/SQLite/sqlite-part-3-reading-database-python.html",completed_percentages=completed_percentages, curLink = TOPIC_DICT["SQLite"][2][1], curTitle=TOPIC_DICT["SQLite"][2][0],  nextLink = TOPIC_DICT["SQLite"][3][1], nextTitle = TOPIC_DICT["SQLite"][3][0],TOPIC_DICT=TOPIC_DICT)
        else:
            update_user_tracking()
            completed_percentages = topic_completion_percent()
            return render_template("tutorials/SQLite/sqlite-part-3-reading-database-python.html",completed_percentages=completed_percentages, curLink = TOPIC_DICT["SQLite"][2][1], curTitle=TOPIC_DICT["SQLite"][2][0],  nextLink = "", nextTitle = "",TOPIC_DICT=TOPIC_DICT)
    except Exception as e:
        return (str(e))



@app.route(TOPIC_DICT["SQLite"][3][1], methods=['GET', 'POST'])
def Graphing_example_from_SQLite():
    lastnum=len(TOPIC_DICT["SQLite"])-1
    try:
        if lastnum>3:
            update_user_tracking()
            completed_percentages = topic_completion_percent()
            return render_template("tutorials/SQLite/graphing-from-sqlite-database.html",completed_percentages=completed_percentages, curLink = TOPIC_DICT["SQLite"][3][1], curTitle=TOPIC_DICT["SQLite"][3][0],  nextLink = TOPIC_DICT["SQLite"][4][1], nextTitle = TOPIC_DICT["SQLite"][4][0],TOPIC_DICT=TOPIC_DICT)
        else:
            update_user_tracking()
            completed_percentages = topic_completion_percent()
            return render_template("tutorials/SQLite/graphing-from-sqlite-database.html",completed_percentages=completed_percentages, curLink = TOPIC_DICT["SQLite"][3][1], curTitle=TOPIC_DICT["SQLite"][3][0],  nextLink = "", nextTitle = "",TOPIC_DICT=TOPIC_DICT)
    except Exception as e:
        return (str(e))



@app.route(TOPIC_DICT["Basics"][0][1], methods=['GET', 'POST'])
def introductions():
    lastnum=len(TOPIC_DICT["Basics"])-1
    try:
        if lastnum>0:
            update_user_tracking()
            completed_percentages = topic_completion_percent()
            return render_template("tutorials/Basics/introductions.html",completed_percentages=completed_percentages, curLink = TOPIC_DICT["Basics"][0][1], curTitle=TOPIC_DICT["Basics"][0][0],  nextLink = TOPIC_DICT["Basics"][1][1], nextTitle = TOPIC_DICT["Basics"][1][0],TOPIC_DICT=TOPIC_DICT)
        else:
            update_user_tracking()
            completed_percentages = topic_completion_percent()
            return render_template("tutorials/Basics/introductions.html",completed_percentages=completed_percentages, curLink = TOPIC_DICT["Basics"][0][1], curTitle=TOPIC_DICT["Basics"][0][0],  nextLink = "", nextTitle = "",TOPIC_DICT=TOPIC_DICT)
    except Exception as e:
        return (str(e))



@app.route(TOPIC_DICT["Basics"][1][1], methods=['GET', 'POST'])
def some_functions():
    lastnum=len(TOPIC_DICT["Basics"])-1
    try:
        if lastnum>1:
            update_user_tracking()
            completed_percentages = topic_completion_percent()
            return render_template("tutorials/Basics/functions.html",completed_percentages=completed_percentages, curLink = TOPIC_DICT["Basics"][1][1], curTitle=TOPIC_DICT["Basics"][1][0],  nextLink = TOPIC_DICT["Basics"][2][1], nextTitle = TOPIC_DICT["Basics"][2][0],TOPIC_DICT=TOPIC_DICT)
        else:
            update_user_tracking()
            completed_percentages = topic_completion_percent()
            return render_template("tutorials/Basics/functions.html",completed_percentages=completed_percentages, curLink = TOPIC_DICT["Basics"][1][1], curTitle=TOPIC_DICT["Basics"][1][0],  nextLink = "", nextTitle = "",TOPIC_DICT=TOPIC_DICT)
    except Exception as e:
        return (str(e))



@app.route(TOPIC_DICT["MySQL"][0][1], methods=['GET', 'POST'])
def Intro_to_MySQL():
    lastnum=len(TOPIC_DICT["MySQL"])-1
    try:
        if lastnum>0:
            update_user_tracking()
            completed_percentages = topic_completion_percent()
            return render_template("tutorials/MySQL/mysql-intro.html",completed_percentages=completed_percentages, curLink = TOPIC_DICT["MySQL"][0][1], curTitle=TOPIC_DICT["MySQL"][0][0],  nextLink = TOPIC_DICT["MySQL"][1][1], nextTitle = TOPIC_DICT["MySQL"][1][0],TOPIC_DICT=TOPIC_DICT)
        else:
            update_user_tracking()
            completed_percentages = topic_completion_percent()
            return render_template("tutorials/MySQL/mysql-intro.html",completed_percentages=completed_percentages, curLink = TOPIC_DICT["MySQL"][0][1], curTitle=TOPIC_DICT["MySQL"][0][0],  nextLink = "", nextTitle = "",TOPIC_DICT=TOPIC_DICT)
    except Exception as e:
        return (str(e))



@app.route(TOPIC_DICT["MySQL"][1][1], methods=['GET', 'POST'])
def Creating_Tables_and_Inserting_Data_with_MySQL():
    lastnum=len(TOPIC_DICT["MySQL"])-1
    try:
        if lastnum>1:
            update_user_tracking()
            completed_percentages = topic_completion_percent()
            return render_template("tutorials/MySQL/create-mysql-tables-insert.html",completed_percentages=completed_percentages, curLink = TOPIC_DICT["MySQL"][1][1], curTitle=TOPIC_DICT["MySQL"][1][0],  nextLink = TOPIC_DICT["MySQL"][2][1], nextTitle = TOPIC_DICT["MySQL"][2][0],TOPIC_DICT=TOPIC_DICT)
        else:
            update_user_tracking()
            completed_percentages = topic_completion_percent()
            return render_template("tutorials/MySQL/create-mysql-tables-insert.html",completed_percentages=completed_percentages, curLink = TOPIC_DICT["MySQL"][1][1], curTitle=TOPIC_DICT["MySQL"][1][0],  nextLink = "", nextTitle = "",TOPIC_DICT=TOPIC_DICT)
    except Exception as e:
        return (str(e))



@app.route(TOPIC_DICT["MySQL"][2][1], methods=['GET', 'POST'])
def Update_Select_and_Delete_with_MySQL():
    lastnum=len(TOPIC_DICT["MySQL"])-1
    try:
        if lastnum>2:
            update_user_tracking()
            completed_percentages = topic_completion_percent()
            return render_template("tutorials/MySQL/mysql-update-select-delete.html",completed_percentages=completed_percentages, curLink = TOPIC_DICT["MySQL"][2][1], curTitle=TOPIC_DICT["MySQL"][2][0],  nextLink = TOPIC_DICT["MySQL"][3][1], nextTitle = TOPIC_DICT["MySQL"][3][0],TOPIC_DICT=TOPIC_DICT)
        else:
            update_user_tracking()
            completed_percentages = topic_completion_percent()
            return render_template("tutorials/MySQL/mysql-update-select-delete.html",completed_percentages=completed_percentages, curLink = TOPIC_DICT["MySQL"][2][1], curTitle=TOPIC_DICT["MySQL"][2][0],  nextLink = "", nextTitle = "",TOPIC_DICT=TOPIC_DICT)
    except Exception as e:
        return (str(e))



@app.route(TOPIC_DICT["MySQL"][3][1], methods=['GET', 'POST'])
def Inserting_Variable_Data_with_MySQL():
    lastnum=len(TOPIC_DICT["MySQL"])-1
    try:
        if lastnum>3:
            update_user_tracking()
            completed_percentages = topic_completion_percent()
            return render_template("tutorials/MySQL/mysql-insert-variable.html",completed_percentages=completed_percentages, curLink = TOPIC_DICT["MySQL"][3][1], curTitle=TOPIC_DICT["MySQL"][3][0],  nextLink = TOPIC_DICT["MySQL"][4][1], nextTitle = TOPIC_DICT["MySQL"][4][0],TOPIC_DICT=TOPIC_DICT)
        else:
            update_user_tracking()
            completed_percentages = topic_completion_percent()
            return render_template("tutorials/MySQL/mysql-insert-variable.html",completed_percentages=completed_percentages, curLink = TOPIC_DICT["MySQL"][3][1], curTitle=TOPIC_DICT["MySQL"][3][0],  nextLink = "", nextTitle = "",TOPIC_DICT=TOPIC_DICT)
    except Exception as e:
        return (str(e))



@app.route(TOPIC_DICT["MySQL"][4][1], methods=['GET', 'POST'])
def Streaming_Tweets_from_Twitter_to_Database():
    lastnum=len(TOPIC_DICT["MySQL"])-1
    try:
        if lastnum>4:
            update_user_tracking()
            completed_percentages = topic_completion_percent()
            return render_template("tutorials/MySQL/mysql-live-database-example-streaming-data.html",completed_percentages=completed_percentages, curLink = TOPIC_DICT["MySQL"][4][1], curTitle=TOPIC_DICT["MySQL"][4][0],  nextLink = TOPIC_DICT["MySQL"][5][1], nextTitle = TOPIC_DICT["MySQL"][5][0],TOPIC_DICT=TOPIC_DICT)
        else:
            update_user_tracking()
            completed_percentages = topic_completion_percent()
            return render_template("tutorials/MySQL/mysql-live-database-example-streaming-data.html",completed_percentages=completed_percentages, curLink = TOPIC_DICT["MySQL"][4][1], curTitle=TOPIC_DICT["MySQL"][4][0],  nextLink = "", nextTitle = "",TOPIC_DICT=TOPIC_DICT)
    except Exception as e:
        return (str(e))



@app.route(TOPIC_DICT["Web dev"][0][1], methods=['GET', 'POST'])
def What_is_web_server():
    lastnum=len(TOPIC_DICT["Web dev"])-1
    try:
        if lastnum>0:
            update_user_tracking()
            completed_percentages = topic_completion_percent()
            return render_template("tutorials/Web dev/webserver.html",completed_percentages=completed_percentages, curLink = TOPIC_DICT["Web dev"][0][1], curTitle=TOPIC_DICT["Web dev"][0][0],  nextLink = TOPIC_DICT["Web dev"][1][1], nextTitle = TOPIC_DICT["Web dev"][1][0],TOPIC_DICT=TOPIC_DICT)
        else:
            update_user_tracking()
            completed_percentages = topic_completion_percent()
            return render_template("tutorials/Web dev/webserver.html",completed_percentages=completed_percentages, curLink = TOPIC_DICT["Web dev"][0][1], curTitle=TOPIC_DICT["Web dev"][0][0],  nextLink = "", nextTitle = "",TOPIC_DICT=TOPIC_DICT)
    except Exception as e:
        return (str(e))



@app.route(TOPIC_DICT["Web dev"][1][1], methods=['GET', 'POST'])
def what_is_html():
    lastnum=len(TOPIC_DICT["Web dev"])-1
    try:
        if lastnum>1:
            update_user_tracking()
            completed_percentages = topic_completion_percent()
            return render_template("tutorials/Web dev/html.html",completed_percentages=completed_percentages, curLink = TOPIC_DICT["Web dev"][1][1], curTitle=TOPIC_DICT["Web dev"][1][0],  nextLink = TOPIC_DICT["Web dev"][2][1], nextTitle = TOPIC_DICT["Web dev"][2][0],TOPIC_DICT=TOPIC_DICT)
        else:
            update_user_tracking()
            completed_percentages = topic_completion_percent()
            return render_template("tutorials/Web dev/html.html",completed_percentages=completed_percentages, curLink = TOPIC_DICT["Web dev"][1][1], curTitle=TOPIC_DICT["Web dev"][1][0],  nextLink = "", nextTitle = "",TOPIC_DICT=TOPIC_DICT)
    except Exception as e:
        return (str(e))





@app.errorhandler(404)
def page_not_found(e):
	try:
		gc.collect()
		rule = request.path
		errorlogging = open("/var/www/FlaskApp/FlaskApp/fourohfour.txt",'w+')
		errorlogging.write((str(rule)+'\n'))
		return render_template("404.html")
	except Exception as e:
		rule = request.path
		flash(str(e)+  str(rule))
		return render_template("404.html")
	
	
	


@app.route("/logout/")
@login_required
def logout():
	session.clear()
	flash("You have been logged out!")
	gc.collect()
	return redirect(url_for("dashboard"))
		
@app.route("/slashboard/")
def slashboard():
	try:
    		return render_template("dashboard.html", TOPIC_DICT = TOIC_DICT )
	except Exception as e:
		return render_template("500.html",error=e)

@app.route("/login/",methods=['GET','POST'])
def login():
	error = ''
	try:
		c, conn = connection()
		if request.method == "POST":
			data = c.execute("SELECT * FROM users WHERE username = (%s)", (thwart(request.form['username']),))
			data = c.fetchone()[2]


			if sha256_crypt.verify(request.form['password'],data):
				session['logged_in'] = True
				session['username'] = request.form['username']
				flash("You are logged in!")
				return redirect(url_for("dashboard"))
				
			else:
				error = "Invalid credentials. Try again."
		gc.collect()
		return render_template("login.html",error=error) ##if login failed, it'll goto here!
	except Exception as e:
		error = "Invalid credentials. Try again."
		#flash(e)
		return render_template("login.html",error = error)


@app.route("/register/",methods=['GET','POST'])
def register():	
	try:
		form = RegisterForm(request.form)
		if request.method == "POST" and form.validate():

			username = form.username.data
			email = form.email.data
			password = sha256_crypt.encrypt((str(form.username.data)))
			c,conn = connection()
			x = c.execute("SELECT * FROM users WHERE username = (%s)", (thwart(username),))
			if int(x)>0:
				flash("that username is already taken, please try another!")
				return render_template("register.html", form = form)
			else:
				c.execute("INSERT INTO users (username, password, email, tracking) VALUES (%s, %s, %s, %s)", (thwart(username), thwart(password), thwart(email), thwart("/introductions/"),))
				#c.execute("INSERT INTO users (username, password, email, tracking) VALUES {0},{1},{2},{3}".format(thwart(username), thwart(password), thwart(email), thwart("/introductions/")))

				conn.commit()
				flash("thanks for registering!")
				c.close()
				conn.close()
				gc.collect()

				session['logged_in'] = True #session is a dictionary to track user action
				session['username'] = username
				
				return redirect(url_for('dashboard'))

		return render_template("register.html", form = form)
	except Exception as e:
		return (str(e))
########example area#########
@app.route('/include_example/')
def include_example():
	replies = {'Jack':'Cool post',
			   'Jane':'+1',
			   'Erika':'Most definitely',
			   'Bob':'wow',
			   'Carl':'amazing!',}
	return render_template("includes_tutorial.html", replies = replies)

@app.route('/converter/')
@app.route('/converter/<int:page>/')
def converter(page=1):
	try:
		return render_template("converterexample.html", page=page)
	except Exception as e:
		return (str(e))

@app.route('/sendmail/')
def send_mail():
	try:	
		
		msg = Message("Send Mail Tutorial!",
		  sender=('103886415@qq.com'),
		  recipients=['jak2017jak@gmail.com'])
		msg.body = "Yo!\nHave you heard the good word of Python???"           
		mail.send(msg)
		return ("Mail sent!")
	except Exception as e:
		return (str(e))
########example area#########
def user_info():
	try:
		client_name=(session['username'])
		guest=False
	except:
		guest=True
		client_name="Guest"
	if not guest:
		try:
			c,conn = connection()
			c.execute("SELECT * FROM users WHERE username = (%s)", (thwart(client_name),))
			data = c.fetchone()
			settings, tracking, rank = data[4], data[5], data[6]
		except Exception as e:
			pass
	else:
		settings, tracking, rank = [0,0], [0,0], [0,0]
	return client_name, settings, tracking, rank

def update_user_tracking():
	try:
		completed = str(request.agrs['completed']) # this arg of ['completed'] is generated in HTML template
		if completed in str(TOPIC_DICT.values()): # url string passed from agr of completed is in TOPIC_DICT url values
			client_name, settings, tracking, rank = user_info()
			if tracking == None:
				tracking =completed
			else:
				if completed not in tracking:
					tracking = tracking + "," + completed
			c, conn = connection()
			c.execute("SELECT * FROM users SET tracking = (%s) WHERE username = (%s)", (thwart(tracking),thwart(client_name),))
			conn.commit()
			c.close()
			conn.close()
			gc.collect()
			client_name, settings, tracking, rank = user_info()
		else:
			pass
	except Exception as e:
		pass

def topic_completion_percent():
	try:
		client_name, settings, tracking, rank = user_info()
		try:
			tracking = tracking.split(",")
		except:
			pass
		if tracking ==None:
			tracking = []

		completed_percentages={}
		
		for each_topic in TOPIC_DICT: # "Basices" "Web dev".....
			total = 0
			total_complete = 0
			for each in TOPIC_DICT[each_topic]: # each episode of below the "Basices" ...
				total += 1
				for done in tracking:
					if done == each[1]:
						total_complete += 1
			percent_complete = int (((total_complete*100)/total))
			completed_percentages[each_topic] = percent_complete
		
		return completed_percentages
	except:
		for each_topic in TOPIC_DICT:
			total = 0
			total_complete = 0
			completed_percentages[each_topic] = 0
		return completed_percentages



class RegisterForm(Form):
	username = TextField('Username',[validators.Length(min=4, max=20)])
	email = TextField('Email',[validators.Length(min=6, max=50)])
	password = PasswordField('New Password',[validators.Required(), validators.EqualTo('confirm',message='Passwords must match.')])
	confirm = PasswordField('repeat Password')
	accept_tos = BooleanField('I accept the <a href="/tos/">Terms of Service</a> and Privacy Notice (updated Jan 22, 2015)', [validators.Required()])
if __name__ == "__main__":
#     app.run(ssl_context=context)
    app.run(debug=True)
