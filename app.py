
from enum import unique
from os import name
from flask import Flask,render_template,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms import validators
from wtforms.validators import Length, ValidationError, input_required

app=Flask(__name__)

app.config['SQLALCHEMY_DARABASE_URI']='sqlite:///database.db'
app.config['SECRET_KEY']="random string"


db=SQLAlchemy(app)     
class Customer(db.Model,UserMixin):
    __tablename__='Customer'
    customer_id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100))
    username=db.Column(db.String(30),nullable=False,unique=True)
    email=db.Column(db.String(100),nullable=True,unique=True)
    password=db.Column(db.String(50),nullable=False)
    number=db.Column(db.Integer,nullable=False)
    addr=db.Column(db.String(200))
    city=db.Column(db.String(200))

class tailor(db.Model,UserMixin):
    __tablename__='tailor'
    tailor_id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100))
    username=db.Column(db.String(30),nullable=False,unique=True)
    email=db.Column(db.String(100),nullable=True,unique=True)
    password=db.Column(db.String(50),nullable=False)
    number=db.Column(db.Integer,nullable=False)
    addr=db.Column(db.String(200))
    city=db.Column(db.String(200))
    skills=db.Column(db.String(400))
    customer_id=db.Column(db.Integer,foreign_key=True)    



class Registerform(FlaskForm):
    username=StringField(validators=[input_required(),Length(min=4,max=20)],render_kw={"placeholder": "username"})
    password=PasswordField(validators=[input_required(),Length(min=4,max=20)],render_kw={"placeholde":"password"})
    submit=SubmitField("register")

    def validate(self, username):
        existing_user_name=Customer.query.filter_by(username=username.data).first()#Checks if username is common
        if existing_user_name:
            raise ValidationError("This username alreay exists please choose another one")
class loginform(FlaskForm):
    username=StringField(validators=[input_required(),Length(min=4,max=20)],render_kw={"placeholder": "username"})
    password=PasswordField(validators=[input_required(),Length(min=4,max=20)],render_kw={"placeholde":"password"})
    submit=SubmitField("register")


def __init__(self,name,city,addr,email,username):
   return Customer('{self.name}','{self.username}')
@app.route('/')

def home():
    return render_template('home.html')

@app.route('/login')

def login():
    return render_template('login.html')


@app.route('/register')

def register():
    return render_template('register.html')

db.init_app(app)
@app.before_first_request
def create_table():
    db.create_all()
    


if __name__=="__main__":
    app.run(debug=True)