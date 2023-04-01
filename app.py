from flask import Flask,request, url_for, redirect, render_template ,session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import pickle
import numpy as np
from model2 import Recommender
import pymysql

app = Flask(__name__)
  



@app.route('/')
def hello_world():
    return render_template("index.html")

# database={'nachi':'123','james':'aac','karthik':'asdsf'}


@app.route('/predict',methods=['POST','GET'])
def predict():
    if request.method == 'POST':
        obj = Recommender()
        movie_name=request.form['movie_name']
        predictions = obj.recommend(movie_name)
        return render_template('recommend.html',pred=predictions)
    else:
        return render_template('index.html')


# @app.route('/form_login',methods=['POST','GET'])
# def login():
#     name1=request.form['username']
#     pwd=request.form['password']
#     if name1 not in database:
#         return render_template('index.html',info='Invalid User')
#     else:
#          if database[name1]!=pwd:
#              return render_template('index.html',info='Invalid Password')
#          else:
#             return render_template('recommend.html',name=name1)
   
# if __name__ == '__main__':
#      app.run(debug='True')



@app.route('/form_login', methods =['GET', 'POST'])
def login():

    mesage = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        conn = pymysql.connect(host='localhost',port=3306,user='root',database='login_cred',password='Hulkhulk_999')
        cur = conn.cursor()
        cur.execute('SELECT * FROM cred WHERE username = % s AND user_password = % s;', (username, password))
        user = cur.fetchall()
        if user:
            mesage = 'Logged in successfully !'
            return render_template('recommend.html', mesage = mesage)
        else:
            mesage = 'Please enter correct email / password !'
    return render_template('index.html', mesage = mesage)

if __name__ == '__main__':
    app.run(debug='True')
