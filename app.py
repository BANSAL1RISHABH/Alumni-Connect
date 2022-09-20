from flask import Flask, render_template, request, session, redirect, flash
from enum import unique
import math
import os
import json
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import pymysql
import mysql.connector
# from flask_mail import Mail
# from werkzeug.utils import secure_filename

pymysql.install_as_MySQLdb()

with open('config.json', 'r') as c:
    params = json.load(c)["params"]

local_server = True
app = Flask(__name__)

app.secret_key = 'super-secret-key'

if local_server:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']

db = SQLAlchemy(app)


class AlumniStudents(db.Model):

    register_no = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(45), unique=False, nullable=False)
    last_name = db.Column(db.String(45), unique=False, nullable=False)
    email_ID = db.Column(db.String(45), unique=True, nullable=False)
    phone_no = db.Column(db.String(12), unique=True, nullable=False)
    college_name = db.Column(db.String(45), unique=False, nullable=True)
    DOB = db.Column(db.String(15), unique=False, nullable=False)
    Gender = db.Column(db.String(80), unique=False, nullable=False)
    password = db.Column(db.String(20), unique=False, nullable=False)
    confirm_password = db.Column(db.String(20), unique=False, nullable=False)
    linkedin_profile = db.Column(db.String(80), unique=False, nullable=True)
    github_profile = db.Column(db.String(80), unique=False, nullable=True)
    other_links = db.Column(db.String(80), unique=False, nullable=True)
    profile_pic = db.Column(db.String(80), unique=False, nullable=True)


@app.route("/")
def home():
    return render_template('login_page.html', params=params)

@app.route("/alumni_profile", methods=['GET', 'POST'])
def alumniSignup():
    if request.method == 'POST':
        '''Add entry to the database'''
        registration_no = request.form.get('reg_no')
        fname = request.form.get('first_name')
        lanme = request.form.get('last_name')
        phone_no = request.form.get('phone')
        email_id = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        dob = request.form.get('dob')
        gender = request.form.get('gender')

        '''
        register_no, first_name, last_name, email_ID, phone_no, college_name, DOB, Gender, password, confirm_password, linkedin_profile, github_profile, other_links, profile_pic
        '''

        entry = AlumniStudents(register_no=registration_no, first_name=fname, last_name=lanme, email_ID=email_id, phone_no=phone_no, DOB = dob, Gender=gender, password=password, confirm_password=confirm_password)

        db.session.add(entry)
        db.session.commit()

    return render_template('alumni_profile.html', params=params)

@app.route('/login_validation', methods=['POST'])
def login_validation():
    print("Method Called")
    
    return render_template('login_page.html', params=params)
    
    return "E-mail: {email}\nPassword: {password}".format(email, password)

@ app.route("/about")
def about():
    return render_template('about.html', params=params)

@ app.route("/contact")
def contact():
    return render_template('contact.html', params=params)


if __name__ == '__main__':
    app.run(debug=True)
