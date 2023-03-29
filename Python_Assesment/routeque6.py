from flask import Flask,request,json,jsonify,render_template
from flask_restful import fields,marshal_with,abort
from question6 import Accessory
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)

USER_INFO={ "user":"1234" }
auth=HTTPBasicAuth()

#security, in order to see the user login details


@auth.verify_password
def verify(username,password):
    validuser=USER_INFO.get(username)==password


@app.route('login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        Password = request.form['Password']

    return login


@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

    return register