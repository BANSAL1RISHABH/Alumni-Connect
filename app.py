import math
import os
import json
from datetime import datetime
from flask import Flask, render_template, request, session, redirect, flash
from flask_sqlalchemy import SQLAlchemy
import pymysql
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

@app.route("/")
def home():
    return render_template('index.html', params=params)

@app.route("/alumni.html")
def alumniconnect():
    return render_template('alumni.html', params=params)

@app.route("/studentProfile.html")
def studentProfile():
    return render_template('studentProfile.html', params=params)

@app.route("/alumniProfile.html")
def alumniProfile():
    return render_template('alumniProfile.html', params=params)

@app.route("/about.html")
def about():
    return render_template('about.html', params=params)

@app.route("/contact.html")
def contact():
    return render_template('contact.html', params=params)


if __name__ == '__main__':
    app.run(debug=True)
