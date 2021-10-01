
from enum import unique
from os import name
import re
from MySQLdb import cursors
import MySQLdb
from MySQLdb.cursors import Cursor
from flask import Flask,render_template,url_for,redirect,request
from flask.helpers import flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask_wtf import FlaskForm
from werkzeug.local import F
from wtforms import StringField,PasswordField,SubmitField, form
from wtforms import validators
from wtforms.fields.core import BooleanField
from wtforms.validators import Email, InputRequired, Length, ValidationError, input_required,email_validator
from flask_bootstrap import Bootstrap
from flask_mysqldb import MySQL
import yaml
 
app=Flask(__name__)


db=SQLAlchemy()
app.config['SQLALCHEMY_DARABASE_URI']='sqlite:///database/Custom.db'
app.config['SECRET_KEY']="random string"

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        User =request.form
        return redirect(url_for("home",usr=home))

    
    return render_template('login.html')
@app.route('/register',methods=['GET', 'POST'])
def register():
   if request.method=='POST':
      
      return 'success'
      
   
   return render_template('register.html')



if __name__=="__main__":
    app.run(debug=True)
    