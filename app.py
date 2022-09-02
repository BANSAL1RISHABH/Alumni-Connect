from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pymysql
import os
import json

pymysql.install_as_MySQLdb()

with open('config.json', 'r') as c:
    params = json.load(c)["params"]

remote_server = True
app = Flask(__name__)



@app.route('/')
def home():
    return render_template('layout.html', params=params)


if __name__ == '__main__':
    app.run(debug=True)


